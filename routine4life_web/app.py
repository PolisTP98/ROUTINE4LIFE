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
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        db = Session(bind=engine)
        medico_data = db.query(medicos).filter(medicos.email == email).first()
        
        if medico_data:
            usuario = db.query(usuarios).filter(
                usuarios.id_medico == medico_data.id_medico,
                usuarios.id_rol == medico_data.id_rol
            ).first()
            
            if usuario and check_password_hash(usuario.contrasena, password):
                if medico_data.id_estatus_usuario == 1: 
                    user = UserMedico(medico_data)
                    login_user(user)
                    flash(f'¡Bienvenido Dr. {medico_data.datos_personales.nombre_completo}!', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Tu cuenta está desactivada. Contacta al administrador.', 'danger')
            else:
                flash('Email o contraseña incorrectos.', 'danger')
        else:
            flash('Email o contraseña incorrectos.', 'danger')
    
    return render_template("login.html")

@app.route("/registro", methods=['GET', 'POST'])
@login_required
def registro():
    if current_user.id_rol != 1:
        flash('No tienes permisos para registrar nuevo personal.', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        db = Session(bind=engine)
        
        try:
            if db.query(medicos).filter(medicos.email == request.form.get('email')).first():
                flash('El email ya esta registrado.', 'danger')
                db.close()
                return redirect(url_for('registro'))
            
            contrasena = request.form.get('contrasena')
            confirmar = request.form.get('confirmar_contrasena')
            
            if contrasena != confirmar:
                flash('Las contrasenas no coinciden.', 'danger')
                db.close()
                return redirect(url_for('registro'))
            
            rol_seleccionado = int(request.form.get('id_rol'))
            
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
            codigo_generado = f"MED-{num:04d}"  # Ejemplo: MED-0001, MED-0002
            
            datos_personales = datos_personales_medico(
                id_sexo=int(request.form.get('id_sexo')),
                id_pais=int(request.form.get('id_pais')),
                nombre_completo=request.form.get('nombre_completo'),
                fecha_nacimiento=datetime.strptime(request.form.get('fecha_nacimiento'), '%Y-%m-%d').date(),
                telefono=telefono_completo,
                fecha_hora_registro=datetime.now()
            )
            db.add(datos_personales)
            db.flush()
            
            nuevo_personal = medicos(
                id_medico=datos_personales.id_medico,
                id_rol=rol_seleccionado,
                id_especialidad=int(request.form.get('id_especialidad')) if rol_seleccionado == 2 else None,
                id_estatus_usuario=1,
                codigo=codigo_generado,
                cedula_profesional=request.form.get('cedula_profesional') if rol_seleccionado == 2 else None,
                email=request.form.get('email'),
                rfc=request.form.get('rfc')
            )
            db.add(nuevo_personal)
            db.flush()
            
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
            
            if rol_seleccionado == 2:
                flash('Medico registrado exitosamente.', 'success')
            elif rol_seleccionado == 4:
                flash('Enfermero registrado exitosamente.', 'success')
            elif rol_seleccionado == 5:
                flash('Recepcionista registrado exitosamente.', 'success')
            
            db.close()
            return redirect(url_for('admin_dashboard'))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al registrar: {str(e)}', 'danger')
            db.close()
            return redirect(url_for('registro'))
    
    # GET: cargar catalogos
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
        # Aquí puedes agregar la lógica de envío de email después
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
    # Redirigir según el rol del usuario
    if current_user.id_rol == 1:  # Medico Administrador
        return redirect(url_for('admin_dashboard'))
    elif current_user.id_rol == 2:  # Medico Regular
        return redirect(url_for('medico_dashboard'))
    elif current_user.id_rol == 4:  # Enfermero
        return redirect(url_for('enfermero_dashboard'))
    elif current_user.id_rol == 5:  # Recepcionista
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
    
    # Obtener medicos con relaciones cargadas (objetos completos)
    medicos_list = db.query(medicos).options(
        joinedload(medicos.datos_personales),
        joinedload(medicos.especialidad)
    ).filter(medicos.id_rol == 2).all()
    
    # Obtener pacientes con relaciones cargadas
    pacientes_list = db.query(pacientes).options(
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.sexo)
    ).filter(
        pacientes.id_medico == current_user.id
    ).all()
    
    # Obtener citas
    proximas_citas = db.query(citas_medicas).options(
        joinedload(citas_medicas.paciente),
        joinedload(citas_medicas.medico),
        joinedload(citas_medicas.estatus)
    ).filter(
        citas_medicas.fecha >= date.today()
    ).order_by(citas_medicas.fecha).limit(10).all()
    
    total_pacientes_admin = len(pacientes_list)
    total_pacientes = db.query(pacientes).count()
    
    db.close()
    
    return render_template("dashboard.html",
                         medicos=medicos_list,
                         pacientes=pacientes_list,
                         proximas_citas=proximas_citas,
                         total_medicos=len(medicos_list),
                         total_pacientes_admin=total_pacientes_admin,
                         total_pacientes=total_pacientes,
                         now_date=date.today())
    
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
        flash('No tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    medico = db.query(medicos).options(
        joinedload(medicos.datos_personales),
        joinedload(medicos.especialidad)
    ).filter(medicos.id_medico == id).first()
    
    if not medico:
        flash('Medico no encontrado.', 'danger')
        db.close()
        return redirect(url_for('gestionar_medicos'))
    
    if request.method == 'POST':
        try:
            # Actualizar datos personales
            medico.datos_personales.nombre_completo = request.form.get('nombre_completo')
            medico.datos_personales.telefono = request.form.get('telefono')
            medico.datos_personales.fecha_nacimiento = datetime.strptime(request.form.get('fecha_nacimiento'), '%Y-%m-%d').date()
            medico.datos_personales.id_sexo = int(request.form.get('id_sexo'))
            
            # Actualizar datos del medico
            medico.email = request.form.get('email')
            medico.rfc = request.form.get('rfc')
            medico.cedula_profesional = request.form.get('cedula_profesional')
            medico.codigo = request.form.get('codigo')
            medico.id_especialidad = int(request.form.get('id_especialidad'))
            
            db.commit()
            flash('Medico actualizado exitosamente.', 'success')
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
    
    from sqlalchemy import func, text
    
    db = Session(bind=engine)
    
    total_medicos = db.query(medicos).filter(medicos.id_rol == 2).count()
    total_enfermeros = db.query(medicos).filter(medicos.id_rol == 4).count()
    total_recepcionistas = db.query(medicos).filter(medicos.id_rol == 5).count()
    total_pacientes = db.query(pacientes).count()
    total_consultas = db.query(consultas_medicas).count()
    
    # Versión alternativa para SQL Server usando DATEPART
    consultas_por_mes = db.query(
        func.concat(func.year(consultas_medicas.fecha), '-', 
                    func.right(func.concat('0', func.month(consultas_medicas.fecha)), 2)).label('mes'),
        func.count().label('total')
    ).group_by(
        func.year(consultas_medicas.fecha),
        func.month(consultas_medicas.fecha)
    ).order_by(
        func.year(consultas_medicas.fecha).desc(),
        func.month(consultas_medicas.fecha).desc()
    ).limit(6).all()
    
    db.close()
    
    return render_template("reportes_generales.html",
                         total_medicos=total_medicos,
                         total_enfermeros=total_enfermeros,
                         total_recepcionistas=total_recepcionistas,
                         total_pacientes=total_pacientes,
                         total_consultas=total_consultas,
                         consultas_por_mes=consultas_por_mes)

# # ==================== DASHBOARD MEDICO ====================

@app.route("/medico/dashboard")
@login_required
def medico_dashboard():
    if current_user.id_rol != 2:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    # Obtener pacientes con sus relaciones cargadas
    pacientes_list = db.query(pacientes).options(
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.sexo)
    ).filter(
        pacientes.id_medico == current_user.id
    ).all()
    
    # Procesar cada paciente para extraer los datos necesarios
    pacientes_data = []
    for paciente in pacientes_list:
        # Obtener última consulta
        ultima = db.query(consultas_medicas).filter(
            consultas_medicas.id_paciente == paciente.id_paciente
        ).order_by(consultas_medicas.fecha.desc()).first()
        
        # Extraer valores a variables simples
        paciente_data = {
            'id': paciente.id_paciente,
            'nombre_completo': paciente.nombre_completo,
            'fecha_nacimiento': paciente.fecha_nacimiento,
            'codigo': paciente.codigo,
            'tipo_diabetes_nombre': paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
            'sexo_nombre': paciente.sexo.nombre if paciente.sexo else None,
            'ultima_consulta': ultima.fecha if ultima else None
        }
        pacientes_data.append(paciente_data)
    
    # Obtener próximas citas con relaciones
    proximas_citas = db.query(citas_medicas).options(
        joinedload(citas_medicas.paciente),
        joinedload(citas_medicas.medico)
    ).filter(
        citas_medicas.id_medico == current_user.id,
        citas_medicas.fecha >= date.today()
    ).order_by(citas_medicas.fecha).limit(5).all()
    
    # Extraer datos de citas a variables simples
    citas_data = []
    for cita in proximas_citas:
        cita_data = {
            'fecha': cita.fecha,
            'hora': cita.hora,
            'paciente_nombre': cita.paciente.nombre_completo if cita.paciente else 'No especificado',
            'motivo': cita.motivo
        }
        citas_data.append(cita_data)
    
    db.close()
    
    return render_template("dashboard_medicos.html",
                         pacientes=pacientes_data,
                         total_pacientes=len(pacientes_data),
                         proximas_citas=citas_data,
                         now_date=date.today())

# ==================== DASHBOARD ENFERMERO ====================
@app.route("/enfermero/dashboard")
@login_required
def enfermero_dashboard():
    # Verificar que sea enfermero
    if current_user.id_rol != 4:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    # Ejemplo: obtener pacientes que requieren atencion
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
    # Verificar que sea recepcionista
    if current_user.id_rol != 5:
        flash('No tienes acceso a esta seccion.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    # Citas de hoy
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
            
            # Generar codigo automatico
            ultimo_paciente = db.query(pacientes).order_by(pacientes.id_paciente.desc()).first()
            if ultimo_paciente:
                try:
                    num = int(ultimo_paciente.codigo.split('-')[-1]) + 1
                except:
                    num = db.query(pacientes).count() + 1
            else:
                num = 1
            codigo_generado = f"PAC-{num:04d}"
            
            nuevo_paciente = pacientes(
                id_medico=current_user.id,
                id_sexo=int(request.form.get('id_sexo')),
                id_estatus_usuario=1,
                id_tipo_diabetes=int(request.form.get('id_tipo_diabetes')) if request.form.get('id_tipo_diabetes') else None,
                codigo=codigo_generado,
                nombre_completo=request.form.get('nombre_completo'),
                fecha_nacimiento=fecha_nac,
                fecha_hora_registro=datetime.now()
            )
            db.add(nuevo_paciente)
            db.commit()
            
            paciente_id = nuevo_paciente.id_paciente
            
            flash('Paciente registrado exitosamente.', 'success')
            db.close()
            return redirect(url_for('detalle_paciente', id=paciente_id))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al registrar paciente: {str(e)}', 'danger')
            db.close()
            return redirect(url_for('medico_dashboard'))
    
    # GET: cargar catalogos
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
        joinedload(pacientes.aplicacion)  # Cargar datos de la app
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
    
    consultas = db.query(consultas_medicas).filter(
        consultas_medicas.id_paciente == id
    ).order_by(consultas_medicas.fecha.desc()).all()
    
    db.close()
    
    return render_template("detalle_paciente.html",
                         paciente=paciente,
                         aplicacion=aplicacion,
                         consultas=consultas,
                         now_date=date.today())

# ==================== CONSULTAS MÉDICAS ====================

@app.route("/paciente/<int:id>/consulta/nueva", methods=['GET', 'POST'])
@login_required
def nueva_consulta(id):
    db = Session(bind=engine)
    
    paciente = db.query(pacientes).filter(
        pacientes.id_paciente == id,
        pacientes.id_medico == current_user.id
    ).first()
    
    if not paciente:
        flash('Paciente no encontrado o no tienes acceso.', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        try:
            nueva_consulta = consultas_medicas(
                id_cita=None, 
                id_medico=current_user.id,
                id_paciente=id,
                fecha=date.today(),
                hora=datetime.now().time(),
                peso=float(request.form.get('peso')) if request.form.get('peso') else None,
                altura=int(request.form.get('altura')) if request.form.get('altura') else None,
                presion_sistolica=int(request.form.get('presion_sistolica')) if request.form.get('presion_sistolica') else None,
                presion_diastolica=int(request.form.get('presion_diastolica')) if request.form.get('presion_diastolica') else None,
                glucosa_ayunas=float(request.form.get('glucosa_ayunas')) if request.form.get('glucosa_ayunas') else None,
                glucosa_postprandial=float(request.form.get('glucosa_postprandial')) if request.form.get('glucosa_postprandial') else None,
                hemoglobina_glicosilada=float(request.form.get('hemoglobina_glicosilada')) if request.form.get('hemoglobina_glicosilada') else None,
                notas=request.form.get('notas'),
                plan_tratamiento=request.form.get('plan_tratamiento')
            )
            db.add(nueva_consulta)
            db.commit()
            flash('Consulta registrada exitosamente.', 'success')
            return redirect(url_for('historial_consulta', id=id))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al registrar consulta: {str(e)}', 'danger')
    
    sintomas_catalogo = db.query(sintomas_diabetes).all()
    return render_template("nueva_consulta.html",
                         paciente=paciente,
                         sintomas=sintomas_catalogo)

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
    
    # Buscar paciente sin filtrar por id_medico
    paciente = db.query(pacientes).filter(pacientes.id_paciente == id).first()
    
    if not paciente:
        flash('Paciente no encontrado.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    # Verificar acceso
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
    
    # Verificar acceso
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
    
#======SINTOMAS========

@app.route("/paciente/<int:id>/sintomas", methods=['GET', 'POST'])
@login_required
def sintomas(id):
    db = Session(bind=engine)
    
    paciente = db.query(pacientes).filter(pacientes.id_paciente == id).first()
    
    if not paciente:
        flash('Paciente no encontrado.', 'danger')
        db.close()
        return redirect(url_for('dashboard'))
    
    # Verificar acceso
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
                sintoma_consulta = sintomas_consulta(
                    id_consulta=consulta.id_consulta,
                    id_sintoma_diabetes=int(sintoma_id),
                    intensidad=request.form.get(f'intensidad_{sintoma_id}'),
                    notas=request.form.get(f'notas_{sintoma_id}')
                )
                db.add(sintoma_consulta)
            
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


#========== CITAS ==========
@app.route("/cita/nueva", methods=['GET', 'POST'])
@login_required
def nueva_cita():
    # Administrador (id_rol=1) y Medico (id_rol=2) pueden agendar citas
    if current_user.id_rol not in [1, 2]:
        flash('No tienes permisos para agendar citas.', 'danger')
        return redirect(url_for('dashboard'))
    
    db = Session(bind=engine)
    
    if request.method == 'POST':
        try:
            # Si es administrador, puede seleccionar cualquier medico
            # Si es medico, se asigna automaticamente
            if current_user.id_rol == 1:
                id_medico = int(request.form.get('id_medico'))
            else:
                id_medico = current_user.id
            
            nueva_cita = citas_medicas(
                id_rol=current_user.id_rol,
                id_medico=id_medico,
                id_paciente=int(request.form.get('id_paciente')),
                id_estatus_cita=1,  # 1 = Pendiente
                fecha=datetime.strptime(request.form.get('fecha'), '%Y-%m-%d').date(),
                hora=datetime.strptime(request.form.get('hora'), '%H:%M').time(),
                motivo=request.form.get('motivo'),
                notas=request.form.get('notas'),
                fecha_hora_solicitud=datetime.now()
            )
            db.add(nueva_cita)
            db.commit()
            flash('Cita agendada exitosamente.', 'success')
            db.close()
            return redirect(url_for('dashboard'))
            
        except Exception as e:
            db.rollback()
            flash(f'Error al agendar cita: {str(e)}', 'danger')
            db.close()
    
    # GET: cargar medicos y pacientes segun el rol
    if current_user.id_rol == 1:  # Administrador
        medicos_list = db.query(medicos).options(
            joinedload(medicos.datos_personales)
        ).filter(
            medicos.id_rol == 2,
            medicos.id_estatus_usuario == 1
        ).all()
        pacientes_list = db.query(pacientes).filter(
            pacientes.id_medico == current_user.id
        ).all()
    elif current_user.id_rol == 2:  # Medico
        medicos_list = [current_user]
        pacientes_list = db.query(pacientes).filter(
            pacientes.id_medico == current_user.id
        ).all()
    else:
        medicos_list = []
        pacientes_list = []
    
    db.close()
    
    return render_template("nueva_cita.html", 
                         medicos=medicos_list, 
                         pacientes=pacientes_list)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)