import sys
import os




carpeta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, carpeta_raiz)

print(f"Ruta raíz agregada: {carpeta_raiz}")

from shared.database import engine
from shared.models import (
    medicos, datos_personales_medico, pacientes, consultas_medicas,
    recetas_medicas, sintomas_consulta, registros_paciente, tipos_registros,
    usuarios, roles_usuarios, estatus_usuarios, especialidades_medicas,
    sexos, tipos_diabetes, sintomas_diabetes, citas_medicas, paises
)

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, date
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import text, extract


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu-clave-secreta-cambia-en-produccion'

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor inicia sesión para acceder'

# Clase wrapper para Flask-Login
class UserMedico(UserMixin):
    def __init__(self, medico_data):
        self.id = medico_data.id_medico
        self.email = medico_data.email
        self.nombre_completo = medico_data.datos_personales.nombre_completo if medico_data.datos_personales else None
        self.id_rol = medico_data.id_rol
    
    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    db = Session(bind=engine)
    medico_data = db.query(medicos).filter(medicos.id_medico == int(user_id)).first()
    if medico_data:
        return UserMedico(medico_data)
    return None

# ==================== RUTAS PÚBLICAS ====================

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Ya tienes una sesión activa. Redirigiendo al dashboard...', 'info')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        # Validar campos vacíos
        if not email or not password:
            flash('Por favor, completa todos los campos para continuar. Ambos, correo y contraseña, son obligatorios.', 'warning')
            return render_template("login.html")
        
        # Validar formato de email
        if '@' not in email or '.' not in email:
            flash('El formato del correo electrónico no es válido. Por favor, usa un formato como: usuario@dominio.com', 'warning')
            return render_template("login.html")
        
        db = Session(bind=engine)
        
        try:
            # Buscar médico por email
            medico_data = db.query(medicos).filter(medicos.email == email).first()
            
            if not medico_data:
                # Mensaje genérico por seguridad
                flash('Credenciales incorrectas. Verifica tu correo electrónico y contraseña.', 'error')
                db.close()
                return render_template("login.html")
            
            # Buscar usuario asociado
            usuario = db.query(usuarios).filter(
                usuarios.id_medico == medico_data.id_medico,
                usuarios.id_rol == medico_data.id_rol
            ).first()
            
            if not usuario:
                flash('Error de autenticación. Por favor, contacta al administrador del sistema.', 'error')
                db.close()
                return render_template("login.html")
            
            # Verificar contraseña
            if check_password_hash(usuario.contrasena, password):
                # Verificar estatus de usuario
                if medico_data.id_estatus_usuario == 1:
                    # Login exitoso
                    user = UserMedico(medico_data)
                    login_user(user)
                    
                    # Mensaje personalizado según el rol
                    nombre_medico = medico_data.datos_personales.nombre_completo if medico_data.datos_personales else "Usuario"
                    
                    if medico_data.id_rol == 1:
                        flash(f'¡Bienvenido al sistema, Administrador {nombre_medico}! Tienes acceso completo a la gestión del sistema.', 'success')
                    elif medico_data.id_rol == 2:
                        flash(f'¡Bienvenido Dr/a. {nombre_medico}! Has iniciado sesión correctamente. Revisa tus pacientes y citas pendientes.', 'success')
                    elif medico_data.id_rol == 4:
                        flash(f'¡Bienvenido/a {nombre_medico}! Tu rol de Enfermero/a te permite registrar signos vitales y datos clínicos.', 'success')
                    elif medico_data.id_rol == 5:
                        flash(f'¡Bienvenido/a {nombre_medico}! Como Recepcionista, puedes gestionar citas y atención a pacientes.', 'success')
                    else:
                        flash(f'¡Bienvenido/a {nombre_medico}! Has iniciado sesión correctamente en Routine4Life.', 'success')
                    
                    db.close()
                    return redirect(url_for('dashboard'))
                else:
                    # Cuenta desactivada
                    flash('Tu cuenta se encuentra desactivada. Por favor, contacta al administrador del sistema para reactivarla.', 'warning')
            else:
                # Contraseña incorrecta
                flash('Contraseña incorrecta. Por favor, verifica tu contraseña e intenta nuevamente.', 'error')
                
                # Registrar intento fallido (opcional)
                # Log de intento fallido
                print(f"[LOG] Intento fallido de login para: {email}")
                
        except Exception as e:
            # Error del servidor
            flash('Ocurrió un error en el servidor. Por favor, intenta nuevamente más tarde o contacta al administrador.', 'error')
            print(f"Error en login: {str(e)}")
        
        finally:
            db.close()
    
    return render_template("login.html")

@app.route("/registro", methods=['GET', 'POST'])
@login_required
def registro():
    if current_user.id_rol != 1:
        flash('No tienes permisos para registrar nuevo personal. Solo el administrador puede realizar esta acción.', 'warning')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        db = Session(bind=engine)
        
        try:
            # Validar email duplicado
            email = request.form.get('email')
            if db.query(medicos).filter(medicos.email == email).first():
                flash(f'El correo electrónico "{email}" ya está registrado en el sistema. Por favor utiliza otro correo.', 'danger')
                db.close()
                return redirect(url_for('registro'))
            
            # Validar contraseñas
            contrasena = request.form.get('contrasena')
            confirmar = request.form.get('confirmar_contrasena')
            
            if contrasena != confirmar:
                flash('Las contraseñas no coinciden. Por favor verifica e intenta nuevamente.', 'danger')
                db.close()
                return redirect(url_for('registro'))
            
            if len(contrasena) < 6:
                flash('La contraseña debe tener al menos 6 caracteres para garantizar la seguridad de la cuenta.', 'warning')
                db.close()
                return redirect(url_for('registro'))
            
            rol_seleccionado = int(request.form.get('id_rol'))
            
            # Obtener nombre del rol
            rol_nombre = db.query(roles_usuarios).filter(roles_usuarios.id_rol == rol_seleccionado).first()
            rol_texto = rol_nombre.nombre if rol_nombre else "Personal"
            
            # Procesar teléfono
            codigo_pais = request.form.get('codigo_pais')
            telefono = request.form.get('telefono')
            telefono_completo = codigo_pais + telefono if codigo_pais else telefono
            
            # Generar código único
            ultimo_medico = db.query(medicos).order_by(medicos.id_medico.desc()).first()
            if ultimo_medico:
                try:
                    num = int(ultimo_medico.codigo.split('-')[-1]) + 1
                except:
                    num = db.query(medicos).count() + 1
            else:
                num = 1
            codigo_generado = f"MED-{num:04d}"
            
            # Obtener datos del formulario
            nombre_completo = request.form.get('nombre_completo')
            fecha_nacimiento = datetime.strptime(request.form.get('fecha_nacimiento'), '%Y-%m-%d').date()
            id_sexo = int(request.form.get('id_sexo'))
            id_pais = int(request.form.get('id_pais'))
            rfc = request.form.get('rfc')
            
            # Crear datos personales
            datos_personales = datos_personales_medico(
                id_sexo=id_sexo,
                id_pais=id_pais,
                nombre_completo=nombre_completo,
                fecha_nacimiento=fecha_nacimiento,
                telefono=telefono_completo,
                fecha_hora_registro=datetime.now()
            )
            db.add(datos_personales)
            db.flush()
            
            # Crear personal médico
            nuevo_personal = medicos(
                id_medico=datos_personales.id_medico,
                id_rol=rol_seleccionado,
                id_especialidad=int(request.form.get('id_especialidad')) if rol_seleccionado == 2 else None,
                id_estatus_usuario=1,
                codigo=codigo_generado,
                cedula_profesional=request.form.get('cedula_profesional') if rol_seleccionado == 2 else None,
                email=email,
                rfc=rfc
            )
            db.add(nuevo_personal)
            db.flush()
            
            # Crear usuario
            hashed_password = generate_password_hash(contrasena)
            nuevo_usuario = usuarios(
                id_rol=rol_seleccionado,
                id_medico=nuevo_personal.id_medico,
                id_paciente=None,
                contrasena=hashed_password,
                fecha_registro=date.today()
            )
            db.add(nuevo_usuario)
            
            db.commit()
            
            # Obtener información adicional para el mensaje
            especialidad_texto = ""
            if rol_seleccionado == 2:
                especialidad = db.query(especialidades_medicas).filter(
                    especialidades_medicas.id_especialidad == int(request.form.get('id_especialidad'))
                ).first()
                especialidad_texto = f" • Especialidad: {especialidad.nombre}\n" if especialidad else ""
            
            # Mensaje flash personalizado según el rol
            if rol_seleccionado == 2:
                flash(
                    f"MÉDICO REGISTRADO CORRECTAMENTE\n\n"
                    f"Datos del nuevo médico:\n"
                    f"• Nombre: {nombre_completo}\n"
                    f"• Email: {email}\n"
                    f"• RFC: {rfc}\n"
                    f"• Cédula profesional: {request.form.get('cedula_profesional')}\n"
                    f"• Código: {codigo_generado}\n"
                    f"{especialidad_texto}"
                    f"• Teléfono: {telefono_completo}\n\n"
                    f"El médico ya puede iniciar sesión en el sistema.",
                    "success"
                )
            elif rol_seleccionado == 4:
                flash(
                    f"ENFERMERO REGISTRADO CORRECTAMENTE\n\n"
                    f"Datos del nuevo enfermero:\n"
                    f"• Nombre: {nombre_completo}\n"
                    f"• Email: {email}\n"
                    f"• RFC: {rfc}\n"
                    f"• Código: {codigo_generado}\n"
                    f"• Teléfono: {telefono_completo}\n\n"
                    f"El enfermero ya puede iniciar sesión en el sistema.",
                    "success"
                )
            elif rol_seleccionado == 5:
                flash(
                    f"RECEPCIONISTA REGISTRADO CORRECTAMENTE\n\n"
                    f"Datos del nuevo recepcionista:\n"
                    f"• Nombre: {nombre_completo}\n"
                    f"• Email: {email}\n"
                    f"• RFC: {rfc}\n"
                    f"• Código: {codigo_generado}\n"
                    f"• Teléfono: {telefono_completo}\n\n"
                    f"El recepcionista ya puede iniciar sesión en el sistema.",
                    "success"
                )
            
            db.close()
            return redirect(url_for('admin_dashboard'))
            
        except Exception as e:
            db.rollback()
            flash(
                f"ERROR AL REGISTRAR PERSONAL\n\n"
                f"No se pudo completar el registro. Detalle del error:\n"
                f"{str(e)}\n\n"
                f"Por favor verifica los datos e intenta nuevamente.",
                "danger"
            )
            db.close()
            return redirect(url_for('registro'))
    
    # GET: cargar catálogos
    db = Session(bind=engine)
    especialidades = db.query(especialidades_medicas).all()
    sexos_list = db.query(sexos).all()
    paises_list = db.query(paises).order_by(paises.nombre).all()
    roles_list = db.query(roles_usuarios).filter(roles_usuarios.id_rol.in_([2, 4, 5])).all()
    db.close()
    
    return render_template("registro.html", 
                         especialidades=especialidades,
                         sexos=sexos_list,
                         paises=paises_list,
                         roles=roles_list)


@app.route("/recuperar_contrasena", methods=['GET', 'POST'])
def recuperar_contrasena():
    if request.method == 'POST':
        email = request.form.get('email')
        flash('Si el correo existe en nuestro sistema, recibirás instrucciones.', 'info')
        return redirect(url_for('login'))
    
    return render_template("recuperar_contrasena.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('login'))


# ==================== DASHBOARD ====================

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.id_rol == 1:
        return redirect(url_for('admin_dashboard'))
    elif current_user.id_rol == 2:
        return redirect(url_for('medico_dashboard'))
    elif current_user.id_rol == 4:
        return redirect(url_for('enfermero_dashboard'))
    elif current_user.id_rol == 5:
        return redirect(url_for('recepcionista_dashboard'))
    else:
        return redirect(url_for('login'))

# ==================== DASHBOARD ADMINISTRADOR ====================

@app.route("/admin/dashboard")
@login_required
def admin_dashboard():
    if current_user.id_rol != 1:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    try:
        medicos_list = db.query(medicos).options(
            joinedload(medicos.datos_personales),
            joinedload(medicos.especialidad)
        ).filter(medicos.id_rol == 2).all()
        
        pacientes_list = db.query(pacientes).options(
            joinedload(pacientes.tipo_diabetes),
            joinedload(pacientes.sexo)
        ).all()
        
        proximas_citas = db.query(citas_medicas).options(
            joinedload(citas_medicas.paciente),
            joinedload(citas_medicas.medico).joinedload(medicos.datos_personales)
        ).filter(
            citas_medicas.fecha >= date.today(),
            citas_medicas.id_estatus_cita == 1
        ).order_by(citas_medicas.fecha).limit(10).all()
        
        # Consultas por mes - CORREGIDO (sin func.format)
        consultas = db.query(consultas_medicas).all()
        
        consultas_por_mes_dict = {}
        for consulta in consultas:
            if consulta.fecha:
                mes_key = consulta.fecha.strftime('%Y-%m')
                if mes_key not in consultas_por_mes_dict:
                    consultas_por_mes_dict[mes_key] = 0
                consultas_por_mes_dict[mes_key] += 1
        
        consultas_mes_data = []
        for mes_key in sorted(consultas_por_mes_dict.keys(), reverse=True)[:6]:
            anio, mes = mes_key.split('-')
            nombre_mes = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'][int(mes)-1]
            consultas_mes_data.append({
                'mes': f"{nombre_mes} {anio}",
                'total': consultas_por_mes_dict[mes_key]
            })
        
        # Ordenar cronológicamente
        consultas_mes_data.reverse()
        
        total_medicos = len(medicos_list)
        total_pacientes = len(pacientes_list)
        
        # Consultas del mes actual
        mes_actual = date.today().month
        ano_actual = date.today().year
        consultas_mes = 0
        for consulta in consultas:
            if consulta.fecha and consulta.fecha.month == mes_actual and consulta.fecha.year == ano_actual:
                consultas_mes += 1
        
        db.close()
        
        return render_template("admin_dashboard.html",
                             medicos=medicos_list,
                             pacientes=pacientes_list,
                             proximas_citas=proximas_citas,
                             total_medicos=total_medicos,
                             total_pacientes=total_pacientes,
                             consultas_mes=consultas_mes,
                             consultas_por_mes=consultas_mes_data,
                             now_date=date.today())
                             
    except Exception as e:
        db.close()
        flash(f'Error al cargar el dashboard: {str(e)}', 'danger')
        return redirect(url_for('dashboard'))

# ==================== ADMIN - GESTION DE MEDICOS ====================

@app.route("/gestionar_medicos")
@login_required
def gestionar_medicos():
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    medicos_list = db.query(medicos).options(
        joinedload(medicos.datos_personales),
        joinedload(medicos.especialidad)
    ).filter(medicos.id_rol == 2).all()
    
    for m in medicos_list:
        _ = m.datos_personales
        _ = m.especialidad
    
    db.close()
    
    return render_template("gestionar_medicos.html", medicos=medicos_list)

@app.route("/editar_medico/<int:id>", methods=['GET', 'POST'])
@login_required
def editar_medico(id):
    if current_user.id_rol != 1:
        flash('No tienes permisos para editar médicos', 'warning')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    medico = db.query(medicos).options(
        joinedload(medicos.datos_personales),
        joinedload(medicos.especialidad)
    ).filter(medicos.id_medico == id).first()
    
    if not medico:
        flash('Médico no encontrado', 'danger')
        db.close()
        return redirect(url_for('gestionar_medicos'))
    
    if request.method == 'POST':
        try:
            nombre_original = medico.datos_personales.nombre_completo
            
            # Actualizar datos
            medico.datos_personales.nombre_completo = request.form.get('nombre_completo')
            medico.datos_personales.telefono = request.form.get('telefono')
            medico.datos_personales.fecha_nacimiento = datetime.strptime(request.form.get('fecha_nacimiento'), '%Y-%m-%d').date()
            medico.datos_personales.id_sexo = int(request.form.get('id_sexo'))
            medico.email = request.form.get('email')
            medico.rfc = request.form.get('rfc')
            medico.cedula_profesional = request.form.get('cedula_profesional')
            medico.codigo = request.form.get('codigo')
            medico.id_especialidad = int(request.form.get('id_especialidad'))
            
            db.commit()
            
            flash(f'Médico actualizado: {nombre_original} → {medico.datos_personales.nombre_completo}', 'success')
            db.close()
            return redirect(url_for('gestionar_medicos'))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al actualizar: {str(e)}', 'danger')
    
    especialidades = db.query(especialidades_medicas).all()
    sexos_list = db.query(sexos).all()
    db.close()
    
    return render_template("editar_medico.html", 
                         medico=medico, 
                         especialidades=especialidades,
                         sexos=sexos_list)

@app.route("/desactivar_medico/<int:id>")
@login_required
def desactivar_medico(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    medico = db.query(medicos).filter(medicos.id_medico == id).first()
    if medico:
        medico.id_estatus_usuario = 2
        db.commit()
        flash('Medico desactivado exitosamente.', 'success')
    db.close()
    return redirect(url_for('gestionar_medicos'))

@app.route("/activar_medico/<int:id>")
@login_required
def activar_medico(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    medico = db.query(medicos).filter(medicos.id_medico == id).first()
    if medico:
        medico.id_estatus_usuario = 1
        db.commit()
        flash('Medico activado exitosamente.', 'success')
    db.close()
    return redirect(url_for('gestionar_medicos'))

# ==================== ADMIN - GESTION DE ENFERMEROS ====================

@app.route("/gestionar_enfermeros")
@login_required
def gestionar_enfermeros():
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    enfermeros_list = db.query(medicos).options(
        joinedload(medicos.datos_personales)
    ).filter(medicos.id_rol == 4).all()
    
    for e in enfermeros_list:
        _ = e.datos_personales
    
    db.close()
    
    return render_template("gestionar_enfermeros.html", enfermeros=enfermeros_list)

@app.route("/editar_enfermero/<int:id>", methods=['GET', 'POST'])
@login_required
def editar_enfermero(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    enfermero = db.query(medicos).options(
        joinedload(medicos.datos_personales)
    ).filter(medicos.id_medico == id, medicos.id_rol == 4).first()
    
    if not enfermero:
        flash('Enfermero no encontrado.', 'danger')
        db.close()
        return redirect(url_for('gestionar_enfermeros'))
    
    if request.method == 'POST':
        try:
            enfermero.datos_personales.nombre_completo = request.form.get('nombre_completo')
            enfermero.datos_personales.telefono = request.form.get('telefono')
            enfermero.datos_personales.fecha_nacimiento = datetime.strptime(request.form.get('fecha_nacimiento'), '%Y-%m-%d').date()
            enfermero.datos_personales.id_sexo = int(request.form.get('id_sexo'))
            enfermero.email = request.form.get('email')
            enfermero.rfc = request.form.get('rfc')
            enfermero.codigo = request.form.get('codigo')
            
            db.commit()
            flash('Enfermero actualizado exitosamente.', 'success')
            db.close()
            return redirect(url_for('gestionar_enfermeros'))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al actualizar: {str(e)}', 'danger')
    
    sexos_list = db.query(sexos).all()
    db.close()
    
    return render_template("editar_enfermero.html", 
                         enfermero=enfermero, 
                         sexos=sexos_list)

@app.route("/desactivar_enfermero/<int:id>")
@login_required
def desactivar_enfermero(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    enfermero = db.query(medicos).filter(medicos.id_medico == id, medicos.id_rol == 4).first()
    if enfermero:
        enfermero.id_estatus_usuario = 2
        db.commit()
        flash('Enfermero desactivado exitosamente.', 'success')
    db.close()
    return redirect(url_for('gestionar_enfermeros'))

@app.route("/activar_enfermero/<int:id>")
@login_required
def activar_enfermero(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    enfermero = db.query(medicos).filter(medicos.id_medico == id, medicos.id_rol == 4).first()
    if enfermero:
        enfermero.id_estatus_usuario = 1
        db.commit()
        flash('Enfermero activado exitosamente.', 'success')
    db.close()
    return redirect(url_for('gestionar_enfermeros'))

# ==================== ADMIN - GESTION DE RECEPCIONISTAS ====================

@app.route("/gestionar_recepcionistas")
@login_required
def gestionar_recepcionistas():
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    recepcionistas_list = db.query(medicos).options(
        joinedload(medicos.datos_personales)
    ).filter(medicos.id_rol == 5).all()
    
    for r in recepcionistas_list:
        _ = r.datos_personales
    
    db.close()
    
    return render_template("gestionar_recepcionistas.html", recepcionistas=recepcionistas_list)

@app.route("/editar_recepcionista/<int:id>", methods=['GET', 'POST'])
@login_required
def editar_recepcionista(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    recepcionista = db.query(medicos).options(
        joinedload(medicos.datos_personales)
    ).filter(medicos.id_medico == id, medicos.id_rol == 5).first()
    
    if not recepcionista:
        flash('Recepcionista no encontrado.', 'danger')
        db.close()
        return redirect(url_for('gestionar_recepcionistas'))
    
    if request.method == 'POST':
        try:
            recepcionista.datos_personales.nombre_completo = request.form.get('nombre_completo')
            recepcionista.datos_personales.telefono = request.form.get('telefono')
            recepcionista.datos_personales.fecha_nacimiento = datetime.strptime(request.form.get('fecha_nacimiento'), '%Y-%m-%d').date()
            recepcionista.datos_personales.id_sexo = int(request.form.get('id_sexo'))
            recepcionista.email = request.form.get('email')
            recepcionista.rfc = request.form.get('rfc')
            recepcionista.codigo = request.form.get('codigo')
            
            db.commit()
            flash('Recepcionista actualizado exitosamente.', 'success')
            db.close()
            return redirect(url_for('gestionar_recepcionistas'))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al actualizar: {str(e)}', 'danger')
    
    sexos_list = db.query(sexos).all()
    db.close()
    
    return render_template("editar_recepcionista.html", 
                         recepcionista=recepcionista, 
                         sexos=sexos_list)

@app.route("/desactivar_recepcionista/<int:id>")
@login_required
def desactivar_recepcionista(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    recepcionista = db.query(medicos).filter(medicos.id_medico == id, medicos.id_rol == 5).first()
    if recepcionista:
        recepcionista.id_estatus_usuario = 2
        db.commit()
        flash('Recepcionista desactivado exitosamente.', 'success')
    db.close()
    return redirect(url_for('gestionar_recepcionistas'))

@app.route("/activar_recepcionista/<int:id>")
@login_required
def activar_recepcionista(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    recepcionista = db.query(medicos).filter(medicos.id_medico == id, medicos.id_rol == 5).first()
    if recepcionista:
        recepcionista.id_estatus_usuario = 1
        db.commit()
        flash('Recepcionista activado exitosamente.', 'success')
    db.close()
    return redirect(url_for('gestionar_recepcionistas'))

# ==================== REPORTES GENERALES ====================

@app.route("/reportes_generales")
@login_required
def reportes_generales():
    if current_user.id_rol != 1:
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    try:
        total_medicos = db.query(medicos).filter(medicos.id_rol == 2).count()
        total_enfermeros = db.query(medicos).filter(medicos.id_rol == 4).count()
        total_recepcionistas = db.query(medicos).filter(medicos.id_rol == 5).count()
        total_pacientes = db.query(pacientes).count()
        total_consultas = db.query(consultas_medicas).count()
        
        # Consultas por mes - CORREGIDO
        consultas = db.query(consultas_medicas).all()
        
        consultas_por_mes_dict = {}
        for consulta in consultas:
            if consulta.fecha:
                mes_key = consulta.fecha.strftime('%Y-%m')
                if mes_key not in consultas_por_mes_dict:
                    consultas_por_mes_dict[mes_key] = 0
                consultas_por_mes_dict[mes_key] += 1
        
        consultas_mes_data = []
        for mes_key in sorted(consultas_por_mes_dict.keys(), reverse=True)[:6]:
            anio, mes = mes_key.split('-')
            nombre_mes = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'][int(mes)-1]
            consultas_mes_data.append({
                'mes': f"{nombre_mes} {anio}",
                'total': consultas_por_mes_dict[mes_key]
            })
        
        consultas_mes_data.reverse()
        
        db.close()
        
        return render_template("reportes_generales.html",
                             total_medicos=total_medicos,
                             total_enfermeros=total_enfermeros,
                             total_recepcionistas=total_recepcionistas,
                             total_pacientes=total_pacientes,
                             total_consultas=total_consultas,
                             consultas_por_mes=consultas_mes_data)
                             
    except Exception as e:
        db.close()
        flash(f'Error al cargar reportes: {str(e)}', 'danger')
        return redirect(url_for('dashboard'))

# ==================== DASHBOARD MEDICO ====================

@app.route("/medico/dashboard")
@login_required
def medico_dashboard():
    if current_user.id_rol != 2:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    try:
        pacientes_list = db.query(pacientes).filter(
            pacientes.id_medico == current_user.id
        ).all()
        
        pacientes_data = []
        for paciente in pacientes_list:
            ultima = db.query(consultas_medicas).filter(
                consultas_medicas.id_paciente == paciente.id_paciente
            ).order_by(consultas_medicas.fecha.desc()).first()
            
            pacientes_data.append({
                'id': paciente.id_paciente,
                'nombre_completo': paciente.nombre_completo,
                'codigo': paciente.codigo,
                'fecha_nacimiento': paciente.fecha_nacimiento,
                'tipo_diabetes_nombre': paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
                'ultima_consulta': ultima.fecha if ultima else None
            })
        
        proximas_citas = db.query(citas_medicas).options(
            joinedload(citas_medicas.paciente)
        ).filter(
            citas_medicas.id_medico == current_user.id,
            citas_medicas.fecha >= date.today(),
            citas_medicas.id_estatus_cita == 1
        ).order_by(citas_medicas.fecha).limit(10).all()
        
        citas_data = []
        for cita in proximas_citas:
            citas_data.append({
                'id_cita': cita.id_cita,
                'fecha': cita.fecha,
                'hora': cita.hora,
                'paciente_nombre': cita.paciente.nombre_completo if cita.paciente else 'No especificado',
                'paciente_id': cita.id_paciente,
                'motivo': cita.motivo
            })
        
        # Consultas por mes - CORREGIDO (sin func.format)
        consultas = db.query(consultas_medicas).filter(
            consultas_medicas.id_medico == current_user.id
        ).all()
        
        consultas_por_mes_dict = {}
        for consulta in consultas:
            if consulta.fecha:
                mes_key = consulta.fecha.strftime('%Y-%m')
                if mes_key not in consultas_por_mes_dict:
                    consultas_por_mes_dict[mes_key] = 0
                consultas_por_mes_dict[mes_key] += 1
        
        consultas_mes_data = []
        for mes_key in sorted(consultas_por_mes_dict.keys(), reverse=True)[:6]:
            anio, mes = mes_key.split('-')
            nombre_mes = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'][int(mes)-1]
            consultas_mes_data.append({
                'mes': f"{nombre_mes} {anio}",
                'total': consultas_por_mes_dict[mes_key]
            })
        
        # Ordenar cronológicamente
        consultas_mes_data.reverse()
        
        db.close()
        
        return render_template("medico_dashboard.html",
                             pacientes=pacientes_data,
                             total_pacientes=len(pacientes_data),
                             proximas_citas=citas_data,
                             consultas_por_mes=consultas_mes_data,
                             now_date=date.today())
                             
    except Exception as e:
        db.close()
        flash(f'Error al cargar el dashboard: {str(e)}', 'danger')
        return redirect(url_for('dashboard'))

# ==================== DASHBOARD ENFERMERO ====================

@app.route("/enfermero/dashboard")
@login_required
def enfermero_dashboard():
    if current_user.id_rol != 4:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    pacientes_recientes = db.query(pacientes).order_by(
        pacientes.fecha_hora_registro.desc()
    ).limit(10).all()
    
    db.close()
    
    return render_template("enfermero/dashboard.html",
                         pacientes_recientes=pacientes_recientes,
                         now_date=date.today())

# ==================== DASHBOARD RECEPCIONISTA ====================

@app.route("/recepcionista/dashboard")
@login_required
def recepcionista_dashboard():
    if current_user.id_rol != 5:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    citas_hoy = db.query(citas_medicas).filter(
        citas_medicas.fecha == date.today()
    ).order_by(citas_medicas.hora).all()
    
    db.close()
    
    return render_template("recepcionista/dashboard.html",
                         citas_hoy=citas_hoy,
                         now_date=date.today())

# ==================== GESTIÓN DE PACIENTES ====================

@app.route("/paciente/nuevo", methods=['GET', 'POST'])
@login_required
def nuevo_paciente():
    if request.method == 'POST':
        db = Session(bind=engine)
        
        try:
            fecha_nac = datetime.strptime(request.form.get('fecha_nacimiento'), '%Y-%m-%d').date()
            
            # ELIMINA ESTA VALIDACIÓN DE EDAD
            # Validar edad - COMENTAR O ELIMINAR ESTAS LÍNEAS
            # hoy = date.today()
            # edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            # if edad < 18:
            #     flash('El paciente debe ser mayor de 18 años', 'warning')
            #     db.close()
            #     return redirect(url_for('nuevo_paciente'))
            
            # Generar código automático
            ultimo_paciente = db.query(pacientes).order_by(pacientes.id_paciente.desc()).first()
            if ultimo_paciente:
                try:
                    num = int(ultimo_paciente.codigo.split('-')[-1]) + 1
                except:
                    num = db.query(pacientes).count() + 1
            else:
                num = 1
            codigo_generado = f"PAC-{num:04d}"
            
            nombre_paciente = request.form.get('nombre_completo')
            id_sexo = int(request.form.get('id_sexo'))
            id_tipo_diabetes = request.form.get('id_tipo_diabetes')
            
            nuevo_pac = pacientes(
                id_medico=current_user.id,
                id_sexo=id_sexo,
                id_estatus_usuario=1,
                id_tipo_diabetes=int(id_tipo_diabetes) if id_tipo_diabetes else None,
                codigo=codigo_generado,
                nombre_completo=nombre_paciente,
                fecha_nacimiento=fecha_nac,
                fecha_hora_registro=datetime.now()
            )
            db.add(nuevo_pac)
            db.commit()
            
            paciente_id = nuevo_pac.id_paciente
            
            flash(f'Paciente registrado: {nombre_paciente} (Código: {codigo_generado})', 'success')
            db.close()
            return redirect(url_for('detalle_paciente', id=paciente_id))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al registrar: {str(e)}', 'danger')
            db.close()
            return redirect(url_for('nuevo_paciente'))
    
    # GET: cargar catálogos
    db = Session(bind=engine)
    sexos_list = db.query(sexos).all()
    tipos_diabetes_list = db.query(tipos_diabetes).all()
    db.close()
    
    return render_template("nuevo_paciente.html",
                         sexos=sexos_list,
                         tipos_diabetes=tipos_diabetes_list)
    
@app.route("/paciente/<int:id>")
@login_required
def detalle_paciente(id):
    db = Session(bind=engine)
    
    paciente = db.query(pacientes).options(
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.sexo),
        joinedload(pacientes.aplicacion)
    ).filter(
        pacientes.id_paciente == id,
        pacientes.id_medico == current_user.id
    ).first()
    
    if not paciente:
        flash('Paciente no encontrado o no tienes acceso.', 'danger')
        db.close()
        if current_user.id_rol == 1:
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('medico_dashboard'))
    
    aplicacion = paciente.aplicacion
    
    # Obtener consultas
    consultas = db.query(consultas_medicas).filter(
        consultas_medicas.id_paciente == id
    ).order_by(consultas_medicas.fecha.desc()).all()
    
    # Obtener citas PENDIENTES (estado 1 = Programada) que NO tienen consulta asociada
    citas_pendientes = db.query(citas_medicas).options(
        joinedload(citas_medicas.consulta)
    ).filter(
        citas_medicas.id_paciente == id,
        citas_medicas.id_estatus_cita == 1,  # Programada
        citas_medicas.fecha >= date.today()  # Solo futuras o hoy
    ).order_by(citas_medicas.fecha.asc(), citas_medicas.hora.asc()).all()
    
    db.close()
    
    return render_template("detalle_paciente.html",
                         paciente=paciente,
                         aplicacion=aplicacion,
                         consultas=consultas,
                         citas_pendientes=citas_pendientes,
                         now_date=date.today())

# ==================== CONSULTAS MÉDICAS ====================

@app.route("/paciente/<int:id>/consulta/nueva", methods=['GET', 'POST'])
@login_required
def nueva_consulta(id):
    cita_id = request.args.get('cita_id', type=int)
    
    if not cita_id:
        flash('Debe seleccionar una cita primero.', 'warning')
        return redirect(url_for('detalle_paciente', id=id))
    
    db = Session(bind=engine)
    
    # Verificar que la cita existe y pertenece al paciente
    cita = db.query(citas_medicas).filter(
        citas_medicas.id_cita == cita_id,
        citas_medicas.id_paciente == id
    ).first()
    
    if not cita:
        flash('Cita no encontrada.', 'danger')
        db.close()
        return redirect(url_for('detalle_paciente', id=id))
    
    # Verificar que no tenga consulta ya
    consulta_existente = db.query(consultas_medicas).filter(
        consultas_medicas.id_cita == cita_id
    ).first()
    
    if consulta_existente:
        flash('Esta cita ya tiene una consulta registrada.', 'warning')
        db.close()
        return redirect(url_for('detalle_paciente', id=id))
    
    paciente = db.query(pacientes).filter(pacientes.id_paciente == id).first()
    
    if request.method == 'POST':
        try:
            nueva_consulta = consultas_medicas(
                id_cita=cita_id,
                id_medico=current_user.id,
                id_paciente=id,
                fecha=date.today(),
                hora=datetime.now().time(),
                peso=float(request.form.get('peso')) if request.form.get('peso') else None,
                altura=int(request.form.get('altura')) if request.form.get('altura') else None,
                presion_sistolica=int(request.form.get('presion_sistolica')) if request.form.get('presion_sistolica') else None,
                presion_diastolica=int(request.form.get('presion_diastolica')) if request.form.get('presion_diastolica') else None,
                frecuencia_cardiaca=int(request.form.get('frecuencia_cardiaca')) if request.form.get('frecuencia_cardiaca') else None,
                glucosa_ayunas=float(request.form.get('glucosa_ayunas')) if request.form.get('glucosa_ayunas') else None,
                glucosa_postprandial=float(request.form.get('glucosa_postprandial')) if request.form.get('glucosa_postprandial') else None,
                hemoglobina_glicosilada=float(request.form.get('hemoglobina_glicosilada')) if request.form.get('hemoglobina_glicosilada') else None,
                colesterol_total=float(request.form.get('colesterol_total')) if request.form.get('colesterol_total') else None,
                trigliceridos=float(request.form.get('trigliceridos')) if request.form.get('trigliceridos') else None,
                nivel_insulina=float(request.form.get('nivel_insulina')) if request.form.get('nivel_insulina') else None,
                notas=request.form.get('notas'),
                plan_tratamiento=request.form.get('plan_tratamiento')
            )
            db.add(nueva_consulta)
            
            # Actualizar el estado de la cita a "Completada" (id_estatus_cita = 3)
            cita.id_estatus_cita = 3  # Completada
            
            db.commit()
            flash('Consulta registrada exitosamente.', 'success')
            db.close()
            return redirect(url_for('detalle_paciente', id=id))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al registrar consulta: {str(e)}', 'danger')
            db.close()
            return redirect(url_for('nueva_consulta', id=id, cita_id=cita_id))
    
    sintomas_catalogo = db.query(sintomas_diabetes).all()
    db.close()
    
    return render_template("nueva_consulta.html", 
                         paciente=paciente,
                         sintomas=sintomas_catalogo,
                         cita=cita)

@app.route("/paciente/<int:id>/historial_consultas")
@login_required
def historial_consulta(id):
    db = Session(bind=engine)
    
    paciente = db.query(pacientes).options(
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.sexo)
    ).filter(
        pacientes.id_paciente == id,
        pacientes.id_medico == current_user.id
    ).first()
    
    if not paciente:
        flash('No tienes acceso a este paciente.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    tipo_diabetes_nombre = paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None
    sexo_nombre = paciente.sexo.nombre if paciente.sexo else None
    
    consultas = db.query(consultas_medicas).filter(
        consultas_medicas.id_paciente == id
    ).order_by(consultas_medicas.fecha.desc()).all()
    
    db.close()
    
    return render_template("historial_consulta.html",
                         paciente=paciente,
                         tipo_diabetes_nombre=tipo_diabetes_nombre,
                         sexo_nombre=sexo_nombre,
                         consultas=consultas)

# ==================== REGISTROS CLÍNICOS ====================

@app.route("/paciente/<int:id>/datos_clinicos", methods=['GET', 'POST'])
@login_required
def datos_clinicos(id):
    db = Session(bind=engine)
    
    paciente = db.query(pacientes).filter(pacientes.id_paciente == id).first()
    
    if not paciente:
        flash('Paciente no encontrado.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    consulta_previa = db.query(consultas_medicas).filter(
        consultas_medicas.id_paciente == id,
        consultas_medicas.id_medico == current_user.id
    ).first()
    
    if not consulta_previa:
        flash('No tienes acceso a este paciente.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        try:
            if request.form.get('glucosa_ayunas'):
                registro = registros_paciente(
                    id_paciente=id,
                    id_tipo_registro=1,
                    fecha=date.today(),
                    hora=datetime.now().time(),
                    valor=float(request.form.get('glucosa_ayunas')),
                    notas='Glucosa en ayunas'
                )
                db.add(registro)
            
            if request.form.get('glucosa_postprandial'):
                registro = registros_paciente(
                    id_paciente=id,
                    id_tipo_registro=1,
                    fecha=date.today(),
                    hora=datetime.now().time(),
                    valor=float(request.form.get('glucosa_postprandial')),
                    notas='Glucosa postprandial'
                )
                db.add(registro)
            
            db.commit()
            flash('Datos clinicos registrados exitosamente.', 'success')
            
        except Exception as e:
            db.rollback()
            flash(f'Error al registrar datos: {str(e)}', 'danger')
    
    historial = db.query(registros_paciente).filter(
        registros_paciente.id_paciente == id
    ).order_by(registros_paciente.fecha.desc()).all()
    
    db.close()
    
    return render_template("datos_clinicos.html",
                         paciente=paciente,
                         historial=historial)

# ==================== TRATAMIENTOS ====================

@app.route("/paciente/<int:id>/tratamiento")
@login_required
def tratamiento(id):
    db = Session(bind=engine)
    
    paciente = db.query(pacientes).filter(pacientes.id_paciente == id).first()
    
    if not paciente:
        flash('Paciente no encontrado.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    consulta_previa = db.query(consultas_medicas).filter(
        consultas_medicas.id_paciente == id,
        consultas_medicas.id_medico == current_user.id
    ).first()
    
    if not consulta_previa:
        flash('No tienes acceso a este paciente.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    consultas_tratamientos = db.query(consultas_medicas).filter(
        consultas_medicas.id_paciente == id,
        consultas_medicas.plan_tratamiento.isnot(None)
    ).order_by(consultas_medicas.fecha.desc()).all()
    
    db.close()
    
    return render_template("tratamiento_paciente.html",
                         paciente=paciente,
                         tratamientos=consultas_tratamientos)

# ==================== SÍNTOMAS ====================

@app.route("/paciente/<int:id>/sintomas", methods=['GET', 'POST'])
@login_required
def sintomas(id):
    db = Session(bind=engine)
    
    paciente = db.query(pacientes).filter(pacientes.id_paciente == id).first()
    
    if not paciente:
        flash('Paciente no encontrado.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    consulta_previa = db.query(consultas_medicas).filter(
        consultas_medicas.id_paciente == id,
        consultas_medicas.id_medico == current_user.id
    ).first()
    
    if not consulta_previa:
        flash('No tienes acceso a este paciente.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        try:
            consulta = db.query(consultas_medicas).filter(
                consultas_medicas.id_paciente == id,
                consultas_medicas.fecha == date.today()
            ).first()
            
            if not consulta:
                consulta = consultas_medicas(
                    id_medico=current_user.id,
                    id_paciente=id,
                    fecha=date.today(),
                    hora=datetime.now().time()
                )
                db.add(consulta)
                db.flush()
            
            sintomas_ids = request.form.getlist('sintomas')
            for sintoma_id in sintomas_ids:
                sintoma_consulta_obj = sintomas_consulta(
                    id_consulta=consulta.id_consulta,
                    id_sintoma_diabetes=int(sintoma_id),
                    intensidad=request.form.get(f'intensidad_{sintoma_id}'),
                    notas=request.form.get(f'notas_{sintoma_id}')
                )
                db.add(sintoma_consulta_obj)
            
            db.commit()
            flash('Sintomas registrados exitosamente.', 'success')
            
        except Exception as e:
            db.rollback()
            flash(f'Error al registrar sintomas: {str(e)}', 'danger')
    
    sintomas_catalogo = db.query(sintomas_diabetes).all()
    db.close()
    
    return render_template("sintomas_detalle.html",
                         paciente=paciente,
                         sintomas_catalogo=sintomas_catalogo)

# ==================== CITAS ====================

from sqlalchemy import text

@app.route("/cita/nueva", methods=['GET', 'POST'])
@login_required
def nueva_cita():
    if current_user.id_rol not in [1, 2]:
        flash('No tienes permisos para agendar citas.', 'warning')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    if request.method == 'POST':
        try:
            if current_user.id_rol == 1:
                id_medico = int(request.form.get('id_medico'))
            else:
                id_medico = current_user.id
            
            id_paciente = int(request.form.get('id_paciente'))
            fecha = datetime.strptime(request.form.get('fecha'), '%Y-%m-%d').date()
            hora = datetime.strptime(request.form.get('hora'), '%H:%M').time()
            motivo = request.form.get('motivo')
            notas = request.form.get('notas')
            
            # Validar que la fecha no sea pasada
            if fecha < date.today():
                flash('No se pueden agendar citas en fechas pasadas', 'warning')
                db.close()
                return redirect(url_for('nueva_cita'))
            
            # Validar horario (8:00 a 20:00)
            if hora.hour < 8 or hora.hour > 20 or (hora.hour == 20 and hora.minute > 0):
                flash('Horario disponible: 8:00 a 20:00', 'warning')
                db.close()
                return redirect(url_for('nueva_cita'))
            
            # Obtener datos para el mensaje
            medico = db.query(medicos).filter(medicos.id_medico == id_medico).first()
            paciente = db.query(pacientes).filter(pacientes.id_paciente == id_paciente).first()
            
            if not paciente:
                flash('Paciente no encontrado', 'danger')
                db.close()
                return redirect(url_for('nueva_cita'))
            
            with engine.connect() as conn:
                stmt = text("""
                    INSERT INTO r4l.citas_medicas 
                    (id_rol, id_medico, id_paciente, id_estatus_cita, fecha, hora, motivo, notas, fecha_hora_solicitud)
                    VALUES (:id_rol, :id_medico, :id_paciente, :id_estatus_cita, :fecha, :hora, :motivo, :notas, :fecha_hora_solicitud)
                """)
                
                conn.execute(stmt, {
                    'id_rol': current_user.id_rol,
                    'id_medico': id_medico,
                    'id_paciente': id_paciente,
                    'id_estatus_cita': 1,
                    'fecha': fecha,
                    'hora': hora,
                    'motivo': motivo,
                    'notas': notas,
                    'fecha_hora_solicitud': datetime.now()
                })
                conn.commit()
            
            nombre_medico = medico.datos_personales.nombre_completo if medico and medico.datos_personales else "Médico"
            db.close()
            
            flash(f'Cita agendada: {paciente.nombre_completo} con {nombre_medico} para el {fecha} a las {hora.strftime("%H:%M")}', 'success')
            return redirect(url_for('dashboard'))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al agendar cita: {str(e)}', 'danger')
            db.close()
            return redirect(url_for('nueva_cita'))
    
    # GET: cargar datos según el rol
    if current_user.id_rol == 1:  # Administrador
        medicos_list = db.query(medicos).options(
            joinedload(medicos.datos_personales),
            joinedload(medicos.especialidad)
        ).filter(
            medicos.id_rol == 2,
            medicos.id_estatus_usuario == 1
        ).all()
        
        # Cargar pacientes agrupados por médico
        pacientes_por_medico = {}
        for medico in medicos_list:
            pacientes_del_medico = db.query(pacientes).filter(
                pacientes.id_medico == medico.id_medico,
                pacientes.id_estatus_usuario == 1
            ).all()
            pacientes_por_medico[medico.id_medico] = [
                {'id': p.id_paciente, 'nombre': p.nombre_completo}
                for p in pacientes_del_medico
            ]
        
        db.close()
        return render_template("nueva_cita.html",
                             medicos=medicos_list,
                             pacientes_por_medico=pacientes_por_medico)
    
    else:  # Médico (rol 2)
        medicos_list = [current_user]
        pacientes_list = db.query(pacientes).filter(
            pacientes.id_medico == current_user.id,
            pacientes.id_estatus_usuario == 1
        ).all()
        
        db.close()
        return render_template("nueva_cita.html",
                             medicos=medicos_list,
                             pacientes=pacientes_list)
        
# ==================== ADMIN - GESTION DE CITAS ====================

@app.route("/admin/gestionar_citas")
@login_required
def admin_gestionar_citas():
    if current_user.id_rol != 1:
        flash('No tienes acceso a esta sección.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    # Obtener todas las citas (futuras y pasadas)
    citas = db.query(citas_medicas).options(
        joinedload(citas_medicas.paciente),
        joinedload(citas_medicas.medico).joinedload(medicos.datos_personales),
        joinedload(citas_medicas.estatus)
    ).order_by(citas_medicas.fecha.desc(), citas_medicas.hora.desc()).all()
    
    # Obtener médicos para el filtro
    medicos_list = db.query(medicos).options(
        joinedload(medicos.datos_personales)
    ).filter(medicos.id_rol == 2).all()
    
    db.close()
    
    return render_template("admin_gestionar_citas.html", 
                         citas=citas, 
                         medicos=medicos_list,
                         now_date=date.today())


@app.route("/admin/editar_cita/<int:id>", methods=['GET', 'POST'])
@login_required
def admin_editar_cita(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso a esta sección.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    cita = db.query(citas_medicas).options(
        joinedload(citas_medicas.paciente),
        joinedload(citas_medicas.medico).joinedload(medicos.datos_personales)  # ← Cargar datos_personales del médico
    ).filter(citas_medicas.id_cita == id).first()
    
    if not cita:
        flash('Cita no encontrada.', 'danger')
        db.close()
        return redirect(url_for('admin_gestionar_citas'))
    
    paciente_nombre = cita.paciente.nombre_completo if cita.paciente else '-'
    medico_nombre = cita.medico.datos_personales.nombre_completo if cita.medico and cita.medico.datos_personales else '-'
    
    if request.method == 'POST':
        try:
            nueva_fecha = datetime.strptime(request.form.get('fecha'), '%Y-%m-%d').date()
            nueva_hora = datetime.strptime(request.form.get('hora'), '%H:%M').time()
            motivo = request.form.get('motivo')
            notas = request.form.get('notas')
            id_estatus_cita = int(request.form.get('id_estatus_cita'))
            
            # Validar que la fecha no sea pasada (excepto si es para cancelar)
            if id_estatus_cita == 1 and nueva_fecha < date.today():
                flash('No se pueden reprogramar citas en fechas pasadas.', 'warning')
                db.close()
                return redirect(url_for('admin_editar_cita', id=id))
            
            # Actualizar cita
            cita.fecha = nueva_fecha
            cita.hora = nueva_hora
            cita.motivo = motivo
            cita.notas = notas
            cita.id_estatus_cita = id_estatus_cita
            
            db.commit()
            
            # Mensaje según la acción
            if id_estatus_cita == 1:
                flash(f'Cita reprogramada para el {nueva_fecha.strftime("%d/%m/%Y")} a las {nueva_hora.strftime("%H:%M")}', 'success')
            elif id_estatus_cita == 2:
                flash('Cita cancelada correctamente.', 'success')
            elif id_estatus_cita == 3:
                flash('Cita completada y marcada como finalizada.', 'success')
            
            db.close()
            return redirect(url_for('admin_gestionar_citas'))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al actualizar la cita: {str(e)}', 'danger')
            db.close()
            return redirect(url_for('admin_editar_cita', id=id))
    
    estatus_citas = [
        {'id': 1, 'nombre': 'Programada'},
        {'id': 2, 'nombre': 'Cancelada'},
        {'id': 3, 'nombre': 'Completada'}
    ]
    
    cita_data = {
        'id_cita': cita.id_cita,
        'fecha': cita.fecha,
        'hora': cita.hora,
        'motivo': cita.motivo,
        'notas': cita.notas,
        'id_estatus_cita': cita.id_estatus_cita,
        'paciente_nombre': paciente_nombre,
        'medico_nombre': medico_nombre
    }
    
    db.close()
    
    return render_template("admin_editar_cita.html", 
                         cita=cita_data,  # ← Pasar el diccionario en lugar del objeto
                         estatus_citas=estatus_citas,
                         now_date=date.today())


@app.route("/admin/cancelar_cita/<int:id>")
@login_required
def admin_cancelar_cita(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso a esta sección.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    cita = db.query(citas_medicas).filter(citas_medicas.id_cita == id).first()
    
    if cita:
        cita.id_estatus_cita = 2  # Cancelada
        db.commit()
        flash(f'Cita cancelada correctamente.', 'success')
    else:
        flash('Cita no encontrada.', 'danger')
    
    db.close()
    return redirect(url_for('admin_gestionar_citas'))

# ==================== ADMIN - GESTION DE CONSULTAS ====================

@app.route("/admin/gestionar_consultas")
@login_required
def admin_gestionar_consultas():
    if current_user.id_rol != 1:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    # Obtener todas las consultas con sus relaciones
    consultas = db.query(consultas_medicas).options(
        joinedload(consultas_medicas.paciente),
        joinedload(consultas_medicas.medico).joinedload(medicos.datos_personales)
    ).order_by(consultas_medicas.fecha.desc(), consultas_medicas.hora.desc()).all()
    
    # Obtener medicos para el filtro
    medicos_list = db.query(medicos).options(
        joinedload(medicos.datos_personales)
    ).filter(medicos.id_rol == 2).all()
    
    db.close()
    
    return render_template("admin_gestionar_consultas.html", 
                         consultas=consultas,
                         medicos=medicos_list)


@app.route("/admin/ver_consulta/<int:id>")
@login_required
def admin_ver_consulta(id):
    if current_user.id_rol != 1:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    consulta = db.query(consultas_medicas).options(
        joinedload(consultas_medicas.paciente),
        joinedload(consultas_medicas.medico).joinedload(medicos.datos_personales),
        joinedload(consultas_medicas.sintomas).joinedload(sintomas_consulta.sintoma_diabetes)
    ).filter(consultas_medicas.id_consulta == id).first()
    
    if not consulta:
        flash('Consulta no encontrada.', 'danger')
        db.close()
        return redirect(url_for('admin_gestionar_consultas'))
    
    sintomas = consulta.sintomas if consulta.sintomas else []
    
    db.close()
    
    return render_template("admin_ver_consulta.html",
                         consulta=consulta,
                         sintomas=sintomas)
    
# ==================== ELIMINAR CONSULTA ====================

@app.route("/consulta/eliminar/<int:id>")
@login_required
def eliminar_consulta(id):
    db = Session(bind=engine)
    
    consulta = db.query(consultas_medicas).options(
        joinedload(consultas_medicas.paciente)
    ).filter(consultas_medicas.id_consulta == id).first()
    
    if not consulta:
        flash('Consulta no encontrada.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    # Verificar permisos
    if current_user.id_rol == 1:
        # Administrador puede eliminar cualquier consulta
        pass
    elif current_user.id_rol == 2:
        # Medico solo puede eliminar sus propias consultas
        if consulta.id_medico != current_user.id:
            flash('No tienes permiso para eliminar esta consulta.', 'danger')
            db.close()
            return redirect(url_for('dashboard'))
    else:
        # Otros roles no pueden eliminar
        flash('No tienes permiso para eliminar consultas.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    paciente_id = consulta.id_paciente
    
    try:
        # Eliminar síntomas asociados primero
        sintomas = db.query(sintomas_consulta).filter(sintomas_consulta.id_consulta == id).all()
        for s in sintomas:
            db.delete(s)
        
        # Eliminar la consulta
        db.delete(consulta)
        db.commit()
        
        flash('Consulta eliminada correctamente.', 'success')
        
    except Exception as e:
        db.rollback()
        flash(f'Error al eliminar la consulta: {str(e)}', 'danger')
    
    db.close()
    
    # Redirigir según el rol
    if current_user.id_rol == 1:
        return redirect(url_for('admin_gestionar_consultas'))
    else:
        return redirect(url_for('detalle_paciente', id=paciente_id))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)