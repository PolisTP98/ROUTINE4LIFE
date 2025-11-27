from config import Config
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import pyodbc
from controllers.auth_controller import AuthController, requiere_rol 
from controllers.medico_controller import MedicoController
from controllers.pacientes_controller import PacienteController
from models.database import Database  

app = Flask(__name__, static_folder='statics')
app.secret_key = "mysecretkey"

@app.before_request
def session_temporal():
    session.permanent = False

# Ruta de login CORREGIDA
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            # Validaciones básicas
            username = request.form.get('id_user', '').strip()
            password = request.form.get('password', '').strip()
            
            if not username or not password:
                flash("Usuario y contraseña son obligatorios", "warning")
                return render_template('login.html')
            
            result = AuthController.login()
            if result == True:
                return redirect(url_for('home'))
            return render_template('login.html')
            
        except Exception as e:
            print(f"ERROR CRÍTICO en login: {str(e)}")
            flash("Error interno del sistema. Por favor, contacte al administrador.", "danger")
            return render_template('login.html')
    
    return render_template('login.html')

@app.route("/home")
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    conn = None
    cursor = None
    try:
        print("DEBUG: Conectando a BD para home...")
        conn = Config(0)
        cursor = conn.cursor()
        
        if id_rol == 1:  # Médico admin - mostrar médicos
            # DEBUG: Ver qué médicos existen
            query_debug = "SELECT id_medico, username FROM r4l.usuarios WHERE id_estatus = 1"
            medicos_debug = Database.execute_query(query_debug)
            print(f"DEBUG - Médicos en sistema: {medicos_debug}")
            
            medicos = MedicoController.obtener_medicos()
            return render_template('admin/dashboard_admin.html',
                                 medicos=medicos,
                                 usuario=session['user'],
                                 nombre_completo=session.get('nombre_completo', ''),
                                 tipo_usuario=session.get('tipo_usuario', ''))
        
        return render_template('home.html', tablas=tablas, usuario=session['user'])
    
    except Exception as e:
        print(f"DEBUG: Error en home: {str(e)}")
        return f"Error al cargar la página: {str(e)}"
    
@app.route("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada exitosamente", "info")
    return redirect(url_for('login'))

# Ruta para verificar conexión a BD
@app.route("/dbcheck")
def dbcheck():
    conn = None
    cursor = None
    try:
        conn = Config(0)
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        
        return jsonify({"status": "OK", "message": "Conexión exitosa a la base de datos"})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500


@app.route("/registro-medico", methods=['GET', 'POST'])
def registro_medico():
    if request.method == 'POST':
        try:
            datos = {
                'id_sexo': request.form['id_sexo'],
                'id_pais': request.form['id_pais'],
                'id_documento': request.form['id_documento'],
                'numero_identificacion': request.form['numero_identificacion'],
                'nombres': request.form['nombres'],
                'apellido_paterno': request.form['apellido_paterno'],
                'apellido_materno': request.form.get('apellido_materno', ''),
                'fecha_nacimiento': request.form['fecha_nacimiento'],
                'telefono': request.form['telefono'],
                'email_personal': request.form['email_personal'],
                'rfc': request.form.get('rfc', ''),
                'direccion': request.form.get('direccion', '')
            }
            
            # Agregar médico
            MedicoController.agregar_medico(datos)
            
            flash("Médico registrado exitosamente. Ahora puede iniciar sesión.", "success")
            return redirect(url_for('login'))
            
        except Exception as e:
            flash(f"Error al registrar médico: {str(e)}", "danger")
    
    # Obtener datos para los dropdowns
    sexos = PacienteController.obtener_sexos()
    paises = PacienteController.obtener_paises()
    documentos = MedicoController.obtener_documentos_legales()
    
    return render_template('registro_medico.html',
                         sexos=sexos,
                         paises=paises,
                         documentos=documentos)

# Ruta para agregar paciente
@app.route("/medico/agregar-paciente", methods=['GET', 'POST'])
@requiere_rol([1, 2])
def medico_agregar_paciente():
    errores = {}
    datos_formulario = {}
    
    if request.method == 'POST':
        try:
            # Recoger datos del formulario
            datos_formulario = {
                'nombres': request.form.get('nombres', '').strip(),
                'apellido_paterno': request.form.get('apellido_paterno', '').strip(),
                'apellido_materno': request.form.get('apellido_materno', '').strip(),
                'fecha_nacimiento': request.form.get('fecha_nacimiento', '').strip(),
                'id_sexo': request.form.get('id_sexo', '').strip(),
                'id_pais': request.form.get('id_pais', '').strip()
            }
            
            # VALIDACIONES
            import re
            from datetime import datetime
            
            # Validar nombres
            if not datos_formulario['nombres']:
                errores['nombres'] = 'Los nombres son obligatorios'
            elif len(datos_formulario['nombres']) < 2:
                errores['nombres'] = 'Los nombres deben tener al menos 2 caracteres'
            elif len(datos_formulario['nombres']) > 200:
                errores['nombres'] = 'Los nombres no pueden tener más de 200 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['nombres']):
                errores['nombres'] = 'Los nombres solo pueden contener letras y espacios'
            
            # Validar apellido paterno
            if not datos_formulario['apellido_paterno']:
                errores['apellido_paterno'] = 'El apellido paterno es obligatorio'
            elif len(datos_formulario['apellido_paterno']) < 2:
                errores['apellido_paterno'] = 'El apellido paterno debe tener al menos 2 caracteres'
            elif len(datos_formulario['apellido_paterno']) > 100:
                errores['apellido_paterno'] = 'El apellido paterno no puede tener más de 100 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['apellido_paterno']):
                errores['apellido_paterno'] = 'El apellido paterno solo puede contener letras y espacios'
            
            # Validar apellido materno (opcional)
            if datos_formulario['apellido_materno']:
                if len(datos_formulario['apellido_materno']) > 100:
                    errores['apellido_materno'] = 'El apellido materno no puede tener más de 100 caracteres'
                elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$', datos_formulario['apellido_materno']):
                    errores['apellido_materno'] = 'El apellido materno solo puede contener letras y espacios'
            
            # Validar fecha de nacimiento
            if not datos_formulario['fecha_nacimiento']:
                errores['fecha_nacimiento'] = 'La fecha de nacimiento es obligatoria'
            else:
                try:
                    fecha_nac = datetime.strptime(datos_formulario['fecha_nacimiento'], '%Y-%m-%d')
                    hoy = datetime.now()
                    
                    # No puede ser fecha futura
                    if fecha_nac > hoy:
                        errores['fecha_nacimiento'] = 'La fecha de nacimiento no puede ser futura'
                    
                    # Validar edad razonable (0-150 años)
                    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
                    if edad < 0:
                        errores['fecha_nacimiento'] = 'Fecha de nacimiento inválida'
                    elif edad > 150:
                        errores['fecha_nacimiento'] = 'Edad no válida'
                        
                except ValueError:
                    errores['fecha_nacimiento'] = 'Formato de fecha inválido (YYYY-MM-DD)'
            
            # Validar sexo
            if not datos_formulario['id_sexo']:
                errores['id_sexo'] = 'El sexo es obligatorio'
            else:
                # Verificar que el sexo exista en la base de datos
                try:
                    sexos = PacienteController.obtener_sexos()
                    sexo_valido = any(str(sexo[0]) == datos_formulario['id_sexo'] for sexo in sexos)
                    if not sexo_valido:
                        errores['id_sexo'] = 'Sexo seleccionado no válido'
                except:
                    errores['id_sexo'] = 'Error al validar el sexo'
            
            # Validar país
            if not datos_formulario['id_pais']:
                errores['id_pais'] = 'El país es obligatorio'
            else:
                # Verificar que el país exista en la base de datos
                try:
                    paises = PacienteController.obtener_paises()
                    pais_valido = any(str(pais[0]) == datos_formulario['id_pais'] for pais in paises)
                    if not pais_valido:
                        errores['id_pais'] = 'País seleccionado no válido'
                except:
                    errores['id_pais'] = 'Error al validar el país'
            
            # Si no hay errores, guardar en la base de datos
            if not errores:
                datos = {
                    'id_sexo': int(datos_formulario['id_sexo']),
                    'id_pais': int(datos_formulario['id_pais']),
                    'nombres': datos_formulario['nombres'],
                    'apellido_paterno': datos_formulario['apellido_paterno'],
                    'apellido_materno': datos_formulario['apellido_materno'],
                    'fecha_nacimiento': datos_formulario['fecha_nacimiento']
                }
                
                PacienteController.agregar_paciente(datos)
                return redirect(url_for('home'))
            
        except Exception as e:
            print(f"ERROR agregando paciente: {str(e)}")
            errores['general'] = "Error interno del sistema al agregar paciente. Por favor, intente nuevamente."
    
    # GET - Mostrar formulario
    try:
        sexos = PacienteController.obtener_sexos()
        paises = PacienteController.obtener_paises()
        
        return render_template('medico/agregar_paciente.html',
                             datos=datos_formulario,
                             errores=errores,
                             sexos=sexos,
                             paises=paises,
                             tipo_usuario=session.get('tipo_usuario', ''))
    except Exception as e:
        print(f"ERROR cargando formulario agregar paciente: {str(e)}")
        return redirect(url_for('home'))

# Ruta para que admin agregue médicos
@app.route('/admin/agregar-medico', methods=['GET', 'POST'])
def admin_agregar_medico():
    errores = {}
    datos_formulario = {}
    
    try:
        conn = Config(0)
        cursor = conn.cursor()
        
        # Obtener datos para los selects
        try:
            cursor.execute("SELECT id_sexo, nombre FROM sexos")
            sexos = cursor.fetchall()
        except:
            try:
                cursor.execute("SELECT id_sexo, nombre FROM Sexos")
                sexos = cursor.fetchall()
            except:
                try:
                    cursor.execute("SELECT id, nombre FROM sexos")
                    sexos = cursor.fetchall()
                except:
                    sexos = [(1, 'Masculino'), (2, 'Femenino'), (3, 'Otro')]
        
        try:
            cursor.execute("SELECT id_pais, nombre FROM paises")
            paises = cursor.fetchall()
        except:
            try:
                cursor.execute("SELECT id_pais, nombre FROM Paises")
                paises = cursor.fetchall()
            except:
                try:
                    cursor.execute("SELECT id, nombre FROM paises")
                    paises = cursor.fetchall()
                except:
                    paises = [(1, 'México'), (2, 'Estados Unidos')]
        
        try:
            cursor.execute("SELECT id_documento, nombre FROM tipos_documento")
            documentos = cursor.fetchall()
        except:
            try:
                cursor.execute("SELECT id_documento, nombre FROM Tipos_Documento")
                documentos = cursor.fetchall()
            except:
                try:
                    cursor.execute("SELECT id, nombre FROM tipos_documento")
                    documentos = cursor.fetchall()
                except:
                    documentos = [(1, 'INE/IFE'), (2, 'Pasaporte')]
        
        if request.method == 'POST':
            # Recoger datos del formulario
            datos_formulario = {
                'nombres': request.form.get('nombres', '').strip(),
                'apellido_paterno': request.form.get('apellido_paterno', '').strip(),
                'apellido_materno': request.form.get('apellido_materno', '').strip(),
                'fecha_nacimiento': request.form.get('fecha_nacimiento', '').strip(),
                'id_sexo': request.form.get('id_sexo', '').strip(),
                'id_pais': request.form.get('id_pais', '').strip(),
                'id_documento': request.form.get('id_documento', '').strip(),
                'numero_identificacion': request.form.get('numero_identificacion', '').strip(),
                'rfc': request.form.get('rfc', '').strip(),
                'telefono': request.form.get('telefono', '').strip(),
                'email_personal': request.form.get('email_personal', '').strip(),
                'direccion': request.form.get('direccion', '').strip()
            }
            
            # VALIDACIONES
            import re
            from datetime import datetime
            
            # Validar nombres
            if not datos_formulario['nombres']:
                errores['nombres'] = 'Los nombres son obligatorios'
            elif len(datos_formulario['nombres']) < 2:
                errores['nombres'] = 'Los nombres deben tener al menos 2 caracteres'
            elif len(datos_formulario['nombres']) > 200:
                errores['nombres'] = 'Los nombres no pueden tener más de 200 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['nombres']):
                errores['nombres'] = 'Los nombres solo pueden contener letras y espacios'
            
            # Validar apellido paterno
            if not datos_formulario['apellido_paterno']:
                errores['apellido_paterno'] = 'El apellido paterno es obligatorio'
            elif len(datos_formulario['apellido_paterno']) < 2:
                errores['apellido_paterno'] = 'El apellido paterno debe tener al menos 2 caracteres'
            elif len(datos_formulario['apellido_paterno']) > 100:
                errores['apellido_paterno'] = 'El apellido paterno no puede tener más de 100 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['apellido_paterno']):
                errores['apellido_paterno'] = 'El apellido paterno solo puede contener letras y espacios'
            
            # Validar apellido materno (opcional)
            if datos_formulario['apellido_materno']:
                if len(datos_formulario['apellido_materno']) > 100:
                    errores['apellido_materno'] = 'El apellido materno no puede tener más de 100 caracteres'
                elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$', datos_formulario['apellido_materno']):
                    errores['apellido_materno'] = 'El apellido materno solo puede contener letras y espacios'
            
            # Validar fecha de nacimiento
            if not datos_formulario['fecha_nacimiento']:
                errores['fecha_nacimiento'] = 'La fecha de nacimiento es obligatoria'
            else:
                try:
                    fecha_nac = datetime.strptime(datos_formulario['fecha_nacimiento'], '%Y-%m-%d')
                    hoy = datetime.now()
                    
                    # No puede ser fecha futura
                    if fecha_nac > hoy:
                        errores['fecha_nacimiento'] = 'La fecha de nacimiento no puede ser futura'
                    
                    # Edad mínima 18 años, máxima 100 años para médico
                    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
                    if edad < 18:
                        errores['fecha_nacimiento'] = 'El médico debe ser mayor de 18 años'
                    elif edad > 100:
                        errores['fecha_nacimiento'] = 'Edad no válida'
                        
                except ValueError:
                    errores['fecha_nacimiento'] = 'Formato de fecha inválido (YYYY-MM-DD)'
            
            # Validar sexo
            if not datos_formulario['id_sexo']:
                errores['id_sexo'] = 'El sexo es obligatorio'
            else:
                try:
                    cursor.execute("SELECT id_sexo FROM sexos WHERE id_sexo = ?", (datos_formulario['id_sexo'],))
                    if not cursor.fetchone():
                        errores['id_sexo'] = 'Sexo seleccionado no válido'
                except:
                    errores['id_sexo'] = 'Error al validar el sexo'
            
            # Validar país
            if not datos_formulario['id_pais']:
                errores['id_pais'] = 'El país es obligatorio'
            else:
                try:
                    cursor.execute("SELECT id_pais FROM paises WHERE id_pais = ?", (datos_formulario['id_pais'],))
                    if not cursor.fetchone():
                        errores['id_pais'] = 'País seleccionado no válido'
                except:
                    errores['id_pais'] = 'Error al validar el país'
            
            # Validar tipo de documento
            if not datos_formulario['id_documento']:
                errores['id_documento'] = 'El tipo de documento es obligatorio'
            else:
                try:
                    cursor.execute("SELECT id_documento FROM tipos_documento WHERE id_documento = ?", (datos_formulario['id_documento'],))
                    if not cursor.fetchone():
                        errores['id_documento'] = 'Tipo de documento no válido'
                except:
                    errores['id_documento'] = 'Error al validar el tipo de documento'
            
            # Validar número de identificación
            if not datos_formulario['numero_identificacion']:
                errores['numero_identificacion'] = 'El número de identificación es obligatorio'
            elif len(datos_formulario['numero_identificacion']) > 50:
                errores['numero_identificacion'] = 'El número de identificación no puede tener más de 50 caracteres'
            else:
                # Verificar que no exista otro médico con el mismo número
                try:
                    cursor.execute("SELECT id FROM medicos WHERE numero_identificacion = ?", (datos_formulario['numero_identificacion'],))
                    if cursor.fetchone():
                        errores['numero_identificacion'] = 'Este número de identificación ya está registrado'
                except:
                    errores['numero_identificacion'] = 'Error al verificar el número de identificación'
            
            # Validar RFC (opcional)
            if datos_formulario['rfc']:
                if len(datos_formulario['rfc']) != 13:
                    errores['rfc'] = 'El RFC debe tener exactamente 13 caracteres'
                elif not re.match(r'^[A-Z&Ñ]{3,4}[0-9]{6}[A-Z0-9]{3}$', datos_formulario['rfc']):
                    errores['rfc'] = 'El formato del RFC no es válido'
            
            # Validar teléfono
            if not datos_formulario['telefono']:
                errores['telefono'] = 'El teléfono es obligatorio'
            else:
                telefono_limpio = re.sub(r'[\s\-\(\)]', '', datos_formulario['telefono'])
                if not telefono_limpio.isdigit():
                    errores['telefono'] = 'El teléfono debe contener solo números'
                elif len(telefono_limpio) != 10:
                    errores['telefono'] = 'El teléfono debe tener 10 dígitos'
                elif len(datos_formulario['telefono']) > 15:
                    errores['telefono'] = 'El teléfono no puede tener más de 15 caracteres'
            
            # Validar email personal
            if not datos_formulario['email_personal']:
                errores['email_personal'] = 'El email personal es obligatorio'
            elif len(datos_formulario['email_personal']) > 255:
                errores['email_personal'] = 'El email personal no puede tener más de 255 caracteres'
            else:
                email_patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(email_patron, datos_formulario['email_personal']):
                    errores['email_personal'] = 'El formato del email personal no es válido'
                else:
                    # Verificar que no exista otro médico con el mismo email
                    try:
                        cursor.execute("SELECT id FROM medicos WHERE email_personal = ?", (datos_formulario['email_personal'],))
                        if cursor.fetchone():
                            errores['email_personal'] = 'Este email personal ya está registrado'
                    except:
                        errores['email_personal'] = 'Error al verificar el email personal'
            
            # Validar dirección
            if datos_formulario['direccion'] and len(datos_formulario['direccion']) > 500:
                errores['direccion'] = 'La dirección no puede tener más de 500 caracteres'
            
            # Si no hay errores, guardar en la base de datos
            if not errores:
                try:
                    cursor.execute("""
                        INSERT INTO medicos (
                            nombres, apellido_paterno, apellido_materno, fecha_nacimiento,
                            id_sexo, id_pais, id_documento, numero_identificacion, rfc,
                            telefono, email_personal, direccion
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        datos_formulario['nombres'],
                        datos_formulario['apellido_paterno'],
                        datos_formulario['apellido_materno'],
                        datos_formulario['fecha_nacimiento'],
                        datos_formulario['id_sexo'],
                        datos_formulario['id_pais'],
                        datos_formulario['id_documento'],
                        datos_formulario['numero_identificacion'],
                        datos_formulario['rfc'],
                        datos_formulario['telefono'],
                        datos_formulario['email_personal'],
                        datos_formulario['direccion']
                    ))
                    conn.commit()
                    
                    flash('Médico agregado exitosamente', 'success')
                    return redirect(url_for('gestion_medicos'))
                    
                except Exception as e:
                    # SOLO MOSTRAR ALERTA PARA ERRORES DE BD, NO PARA VALIDACIONES
                    flash(f'Error al guardar en la base de datos: {str(e)}', 'danger')
            
            
    except Exception as e:
        flash(f'Error de conexión: {str(e)}', 'danger')
        # Datos estáticos si hay error
        sexos = [(1, 'Masculino'), (2, 'Femenino')]
        paises = [(1, 'México')]
        documentos = [(1, 'INE/IFE')]
    
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
    
    return render_template('admin/agregar_medico.html',
                         datos=datos_formulario,
                         errores=errores,
                         sexos=sexos,
                         paises=paises,
                         documentos=documentos,
                         tipo_usuario=session.get('tipo_usuario', 'Usuario'))

# Ruta para agregar paciente con manejo de errores completo
@app.route("/medico/editar-paciente/<int:id_paciente>", methods=['GET', 'POST'])
@requiere_rol([1, 2])
def medico_editar_paciente(id_paciente):
    errores = {}
    datos_formulario = {}
    
    if request.method == 'POST':
        try:
            # Recoger datos del formulario
            datos_formulario = {
                'nombres': request.form.get('nombres', '').strip(),
                'apellido_paterno': request.form.get('apellido_paterno', '').strip(),
                'apellido_materno': request.form.get('apellido_materno', '').strip(),
                'fecha_nacimiento': request.form.get('fecha_nacimiento', '').strip(),
                'id_sexo': request.form.get('id_sexo', '').strip(),
                'id_pais': request.form.get('id_pais', '').strip()
            }
            
            # VALIDACIONES
            import re
            from datetime import datetime
            
            # Validar nombres
            if not datos_formulario['nombres']:
                errores['nombres'] = 'Los nombres son obligatorios'
            elif len(datos_formulario['nombres']) < 2:
                errores['nombres'] = 'Los nombres deben tener al menos 2 caracteres'
            elif len(datos_formulario['nombres']) > 200:
                errores['nombres'] = 'Los nombres no pueden tener más de 200 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['nombres']):
                errores['nombres'] = 'Los nombres solo pueden contener letras y espacios'
            
            # Validar apellido paterno
            if not datos_formulario['apellido_paterno']:
                errores['apellido_paterno'] = 'El apellido paterno es obligatorio'
            elif len(datos_formulario['apellido_paterno']) < 2:
                errores['apellido_paterno'] = 'El apellido paterno debe tener al menos 2 caracteres'
            elif len(datos_formulario['apellido_paterno']) > 100:
                errores['apellido_paterno'] = 'El apellido paterno no puede tener más de 100 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['apellido_paterno']):
                errores['apellido_paterno'] = 'El apellido paterno solo puede contener letras y espacios'
            
            # Validar apellido materno (opcional)
            if datos_formulario['apellido_materno']:
                if len(datos_formulario['apellido_materno']) > 100:
                    errores['apellido_materno'] = 'El apellido materno no puede tener más de 100 caracteres'
                elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$', datos_formulario['apellido_materno']):
                    errores['apellido_materno'] = 'El apellido materno solo puede contener letras y espacios'
            
            # Validar fecha de nacimiento
            if not datos_formulario['fecha_nacimiento']:
                errores['fecha_nacimiento'] = 'La fecha de nacimiento es obligatoria'
            else:
                try:
                    fecha_nac = datetime.strptime(datos_formulario['fecha_nacimiento'], '%Y-%m-%d')
                    hoy = datetime.now()
                    
                    # No puede ser fecha futura
                    if fecha_nac > hoy:
                        errores['fecha_nacimiento'] = 'La fecha de nacimiento no puede ser futura'
                    
                    # Validar edad razonable (0-150 años)
                    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
                    if edad < 0:
                        errores['fecha_nacimiento'] = 'Fecha de nacimiento inválida'
                    elif edad > 150:
                        errores['fecha_nacimiento'] = 'Edad no válida'
                        
                except ValueError:
                    errores['fecha_nacimiento'] = 'Formato de fecha inválido (YYYY-MM-DD)'
            
            # Validar sexo
            if not datos_formulario['id_sexo']:
                errores['id_sexo'] = 'El sexo es obligatorio'
            else:
                # Verificar que el sexo exista en la base de datos
                try:
                    sexos = PacienteController.obtener_sexos()
                    sexo_valido = any(str(sexo[0]) == datos_formulario['id_sexo'] for sexo in sexos)
                    if not sexo_valido:
                        errores['id_sexo'] = 'Sexo seleccionado no válido'
                except:
                    errores['id_sexo'] = 'Error al validar el sexo'
            
            # Validar país
            if not datos_formulario['id_pais']:
                errores['id_pais'] = 'El país es obligatorio'
            else:
                # Verificar que el país exista en la base de datos
                try:
                    paises = PacienteController.obtener_paises()
                    pais_valido = any(str(pais[0]) == datos_formulario['id_pais'] for pais in paises)
                    if not pais_valido:
                        errores['id_pais'] = 'País seleccionado no válido'
                except:
                    errores['id_pais'] = 'Error al validar el país'
            
            # Si no hay errores, actualizar en la base de datos
            if not errores:
                datos = {
                    'id_sexo': int(datos_formulario['id_sexo']),
                    'id_pais': int(datos_formulario['id_pais']),
                    'nombres': datos_formulario['nombres'],
                    'apellido_paterno': datos_formulario['apellido_paterno'],
                    'apellido_materno': datos_formulario['apellido_materno'],
                    'fecha_nacimiento': datos_formulario['fecha_nacimiento']
                }
                
                PacienteController.actualizar_paciente(id_paciente, datos)
                return redirect(url_for('home'))
            
        except Exception as e:
            print(f"ERROR actualizando paciente {id_paciente}: {str(e)}")
            errores['general'] = "Error interno del sistema al actualizar paciente. Por favor, intente nuevamente."
    
    # GET - Mostrar formulario de edición
    try:
        paciente = PacienteController.obtener_paciente_por_id(id_paciente)
        if not paciente:
            return redirect(url_for('home'))
        
        sexos = PacienteController.obtener_sexos()
        paises = PacienteController.obtener_paises()
        
        # Si es GET y no hay datos del formulario (por POST con errores), usar datos del paciente
        if not datos_formulario or not any(datos_formulario.values()):
            datos_formulario = {
                'nombres': paciente.nombres,
                'apellido_paterno': paciente.apellido_paterno,
                'apellido_materno': paciente.apellido_materno or '',
                'fecha_nacimiento': paciente.fecha_nacimiento.strftime('%Y-%m-%d') if paciente.fecha_nacimiento else '',
                'id_sexo': str(paciente.id_sexo),
                'id_pais': str(paciente.id_pais)
            }
        
        return render_template('medico/editar_paciente.html',
                             paciente=paciente,
                             datos=datos_formulario,
                             errores=errores,
                             sexos=sexos,
                             paises=paises,
                             tipo_usuario=session.get('tipo_usuario', ''))
                             
    except Exception as e:
        print(f"ERROR cargando edición paciente {id_paciente}: {str(e)}")
        return redirect(url_for('home'))
    
@app.route("/medico/lista-pacientes")
@requiere_rol([1, 2])  # Admin y médicos normales
def medico_lista_pacientes():
    try:
        pacientes = PacienteController.obtener_pacientes()
        return render_template('medico/lista_pacientes.html',
                             pacientes=pacientes,
                             tipo_usuario=session.get('tipo_usuario', ''))
    except Exception as e:
        flash(f"Error al cargar pacientes: {str(e)}", "danger")
        return render_template('medico/lista_pacientes.html',
                             pacientes=[],
                             tipo_usuario=session.get('tipo_usuario', ''))
        
## Ruta para eliminar paciente con manejo de errores
@app.route("/medico/eliminar-paciente/<int:id_paciente>")
@requiere_rol([1, 2])
def eliminar_paciente(id_paciente):
    try:
        # Verificar que el paciente existe antes de eliminar
        paciente = PacienteController.obtener_paciente_por_id(id_paciente)
        if not paciente:
            flash("El paciente no existe o ya fue eliminado", "warning")
            return redirect(url_for('home'))
        
        PacienteController.eliminar_paciente(id_paciente)
        flash("Paciente eliminado correctamente", "success")
        
    except Exception as e:
        print(f"ERROR eliminando paciente {id_paciente}: {str(e)}")
        flash("Error al eliminar el paciente", "danger")
    
    return redirect(url_for('home'))

# Ruta para ver pacientes eliminados (solo admin)
@app.route("/admin/pacientes-eliminados")
@requiere_rol([1])  # Solo admin
def pacientes_eliminados():
    try:
        pacientes = PacienteController.obtener_pacientes_eliminados()
        return render_template('admin/pacientes_eliminados.html',
                             pacientes=pacientes,
                             tipo_usuario=session.get('tipo_usuario', ''))
    except Exception as e:
        flash(f"Error al cargar pacientes eliminados: {str(e)}", "danger")
        return redirect(url_for('home'))

# Ruta para reactivar paciente (solo admin)
@app.route("/admin/reactivar-paciente/<int:id_paciente>")
@requiere_rol([1])  # Solo admin
def reactivar_paciente(id_paciente):
    try:
        PacienteController.reactivar_paciente(id_paciente)
        flash("Paciente reactivado correctamente", "success")
    except Exception as e:
        flash(f"Error al reactivar paciente: {str(e)}", "danger")
    return redirect(url_for('pacientes_eliminados'))

# Ruta para editar médico
@app.route("/admin/editar-medico/<int:id_medico>", methods=['GET', 'POST'])
@requiere_rol([1])  # Solo admin
def admin_editar_medico(id_medico):
    errores = {}
    datos_formulario = {}
    
    if request.method == 'POST':
        try:
            # Recoger datos del formulario
            datos_formulario = {
                'id_rol': request.form.get('id_rol', '').strip(),
                'id_sexo': request.form.get('id_sexo', '').strip(),
                'id_pais': request.form.get('id_pais', '').strip(),
                'id_documento': request.form.get('id_documento', '').strip(),
                'numero_identificacion': request.form.get('numero_identificacion', '').strip(),
                'nombres': request.form.get('nombres', '').strip(),
                'apellido_paterno': request.form.get('apellido_paterno', '').strip(),
                'apellido_materno': request.form.get('apellido_materno', '').strip(),
                'fecha_nacimiento': request.form.get('fecha_nacimiento', '').strip(),
                'telefono': request.form.get('telefono', '').strip(),
                'email_personal': request.form.get('email_personal', '').strip(),
                'email_laboral': request.form.get('email_laboral', '').strip(),
                'rfc': request.form.get('rfc', '').strip(),
                'direccion': request.form.get('direccion', '').strip()
            }
            
            # VALIDACIONES
            import re
            from datetime import datetime
            
            # Validar nombres
            if not datos_formulario['nombres']:
                errores['nombres'] = 'Los nombres son obligatorios'
            elif len(datos_formulario['nombres']) < 2:
                errores['nombres'] = 'Los nombres deben tener al menos 2 caracteres'
            elif len(datos_formulario['nombres']) > 200:
                errores['nombres'] = 'Los nombres no pueden tener más de 200 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['nombres']):
                errores['nombres'] = 'Los nombres solo pueden contener letras y espacios'
            
            # Validar apellido paterno
            if not datos_formulario['apellido_paterno']:
                errores['apellido_paterno'] = 'El apellido paterno es obligatorio'
            elif len(datos_formulario['apellido_paterno']) < 2:
                errores['apellido_paterno'] = 'El apellido paterno debe tener al menos 2 caracteres'
            elif len(datos_formulario['apellido_paterno']) > 100:
                errores['apellido_paterno'] = 'El apellido paterno no puede tener más de 100 caracteres'
            elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', datos_formulario['apellido_paterno']):
                errores['apellido_paterno'] = 'El apellido paterno solo puede contener letras y espacios'
            
            # Validar apellido materno (opcional)
            if datos_formulario['apellido_materno']:
                if len(datos_formulario['apellido_materno']) > 100:
                    errores['apellido_materno'] = 'El apellido materno no puede tener más de 100 caracteres'
                elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$', datos_formulario['apellido_materno']):
                    errores['apellido_materno'] = 'El apellido materno solo puede contener letras y espacios'
            
            # Validar fecha de nacimiento
            if not datos_formulario['fecha_nacimiento']:
                errores['fecha_nacimiento'] = 'La fecha de nacimiento es obligatoria'
            else:
                try:
                    fecha_nac = datetime.strptime(datos_formulario['fecha_nacimiento'], '%Y-%m-%d')
                    hoy = datetime.now()
                    
                    if fecha_nac > hoy:
                        errores['fecha_nacimiento'] = 'La fecha de nacimiento no puede ser futura'
                    
                    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
                    if edad < 18:
                        errores['fecha_nacimiento'] = 'El médico debe ser mayor de 18 años'
                    elif edad > 100:
                        errores['fecha_nacimiento'] = 'Edad no válida'
                        
                except ValueError:
                    errores['fecha_nacimiento'] = 'Formato de fecha inválido (YYYY-MM-DD)'
            
            # Validar sexo
            if not datos_formulario['id_sexo']:
                errores['id_sexo'] = 'El sexo es obligatorio'
            
            # Validar país
            if not datos_formulario['id_pais']:
                errores['id_pais'] = 'El país es obligatorio'
            
            # Validar tipo de documento
            if not datos_formulario['id_documento']:
                errores['id_documento'] = 'El tipo de documento es obligatorio'
            
            # Validar número de identificación
            if not datos_formulario['numero_identificacion']:
                errores['numero_identificacion'] = 'El número de identificación es obligatorio'
            elif len(datos_formulario['numero_identificacion']) > 50:
                errores['numero_identificacion'] = 'El número de identificación no puede tener más de 50 caracteres'
            else:
                # Verificar que no exista otro médico con el mismo número (excluyendo el actual)
                try:
                    medico_existente = MedicoController.obtener_medico_por_identificacion(datos_formulario['numero_identificacion'])
                    if medico_existente and medico_existente[0] != id_medico:
                        errores['numero_identificacion'] = 'Este número de identificación ya está registrado por otro médico'
                except:
                    pass
            
            # Validar RFC (opcional)
            if datos_formulario['rfc']:
                if len(datos_formulario['rfc']) != 13:
                    errores['rfc'] = 'El RFC debe tener exactamente 13 caracteres'
                elif not re.match(r'^[A-Z&Ñ]{3,4}[0-9]{6}[A-Z0-9]{3}$', datos_formulario['rfc']):
                    errores['rfc'] = 'El formato del RFC no es válido'
            
            # Validar teléfono
            if not datos_formulario['telefono']:
                errores['telefono'] = 'El teléfono es obligatorio'
            else:
                telefono_limpio = re.sub(r'[\s\-\(\)]', '', datos_formulario['telefono'])
                if not telefono_limpio.isdigit():
                    errores['telefono'] = 'El teléfono debe contener solo números'
                elif len(telefono_limpio) != 10:
                    errores['telefono'] = 'El teléfono debe tener 10 dígitos'
                elif len(datos_formulario['telefono']) > 15:
                    errores['telefono'] = 'El teléfono no puede tener más de 15 caracteres'
            
            # Validar email personal
            if not datos_formulario['email_personal']:
                errores['email_personal'] = 'El email personal es obligatorio'
            elif len(datos_formulario['email_personal']) > 255:
                errores['email_personal'] = 'El email personal no puede tener más de 255 caracteres'
            else:
                email_patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(email_patron, datos_formulario['email_personal']):
                    errores['email_personal'] = 'El formato del email personal no es válido'
                else:
                    # Verificar que no exista otro médico con el mismo email (excluyendo el actual)
                    try:
                        medico_existente = MedicoController.obtener_medico_por_email_personal(datos_formulario['email_personal'])
                        if medico_existente and medico_existente[0] != id_medico:
                            errores['email_personal'] = 'Este email personal ya está registrado por otro médico'
                    except:
                        pass
            
            # Validar email laboral
            if not datos_formulario['email_laboral']:
                errores['email_laboral'] = 'El email laboral es obligatorio'
            elif len(datos_formulario['email_laboral']) > 255:
                errores['email_laboral'] = 'El email laboral no puede tener más de 255 caracteres'
            else:
                email_patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(email_patron, datos_formulario['email_laboral']):
                    errores['email_laboral'] = 'El formato del email laboral no es válido'
                else:
                    # Verificar que no exista otro médico con el mismo email laboral (excluyendo el actual)
                    try:
                        medico_existente = MedicoController.obtener_medico_por_email_laboral(datos_formulario['email_laboral'])
                        if medico_existente and medico_existente[0] != id_medico:
                            errores['email_laboral'] = 'Este email laboral ya está registrado por otro médico'
                    except:
                        pass
            
            # Validar dirección
            if datos_formulario['direccion'] and len(datos_formulario['direccion']) > 500:
                errores['direccion'] = 'La dirección no puede tener más de 500 caracteres'
            
            # Validar rol
            if not datos_formulario['id_rol']:
                errores['id_rol'] = 'El rol es obligatorio'
            
            # Si no hay errores, actualizar en la base de datos
            if not errores:
                datos_actualizar = {
                    'id_rol': int(datos_formulario['id_rol']),
                    'id_sexo': int(datos_formulario['id_sexo']),
                    'id_pais': int(datos_formulario['id_pais']),
                    'id_documento': int(datos_formulario['id_documento']),
                    'numero_identificacion': datos_formulario['numero_identificacion'],
                    'nombres': datos_formulario['nombres'],
                    'apellido_paterno': datos_formulario['apellido_paterno'],
                    'apellido_materno': datos_formulario['apellido_materno'],
                    'fecha_nacimiento': datos_formulario['fecha_nacimiento'],
                    'telefono': datos_formulario['telefono'],
                    'email_personal': datos_formulario['email_personal'],
                    'email_laboral': datos_formulario['email_laboral'],
                    'rfc': datos_formulario['rfc'],
                    'direccion': datos_formulario['direccion']
                }
                
                if MedicoController.actualizar_medico(id_medico, datos_actualizar):
                    flash("Médico actualizado exitosamente", "success")
                    return redirect(url_for('home'))
                else:
                    flash("Error al actualizar el médico", "danger")
            
        except Exception as e:
            flash(f"Error al actualizar médico: {str(e)}", "danger")
    
    # GET - Mostrar formulario de edición
    try:
        medico = MedicoController.obtener_medico_por_id(id_medico)
        
        if not medico:
            flash("Médico no encontrado", "warning")
            return redirect(url_for('home'))
        
        # Obtener datos para dropdowns
        sexos = PacienteController.obtener_sexos()
        paises = PacienteController.obtener_paises()
        documentos = MedicoController.obtener_documentos_legales()
        roles = MedicoController.obtener_roles()
        
        return render_template('admin/editar_medico.html',
                             medico=medico,
                             datos=datos_formulario if request.method == 'POST' else None,
                             errores=errores,
                             sexos=sexos,
                             paises=paises,
                             documentos=documentos,
                             roles=roles,
                             tipo_usuario=session.get('tipo_usuario', ''))
                             
    except Exception as e:
        flash(f"Error al cargar médico: {str(e)}", "danger")
        return redirect(url_for('home'))

# Ruta para eliminar médico (soft delete)
@app.route("/admin/eliminar-medico/<int:id_medico>")
@requiere_rol([1])  # Solo admin
def admin_eliminar_medico(id_medico):
    try:
        # No permitir eliminarse a sí mismo
        if id_medico == session.get('id_medico'):
            flash("No puedes eliminar tu propio usuario", "warning")
            return redirect(url_for('home'))
            
        if MedicoController.eliminar_medico(id_medico):
            flash("Médico eliminado correctamente", "success")
        else:
            flash("Error al eliminar el médico", "danger")
            
    except Exception as e:
        flash(f"Error al eliminar médico: {str(e)}", "danger")
    
    return redirect(url_for('home'))

# Ruta para ver médicos eliminados
@app.route("/admin/medicos-eliminados")
@requiere_rol([1])  # Solo admin
def admin_medicos_eliminados():
    try:
        medicos = MedicoController.obtener_medicos_eliminados()
        return render_template('admin/medicos_eliminados.html',
                             medicos=medicos,
                             tipo_usuario=session.get('tipo_usuario', ''))
    except Exception as e:
        flash(f"Error al cargar médicos eliminados: {str(e)}", "danger")
        return redirect(url_for('home'))

# Ruta para reactivar médico
@app.route("/admin/reactivar-medico/<int:id_medico>")
@requiere_rol([1])  # Solo admin
def admin_reactivar_medico(id_medico):
    try:
        if MedicoController.reactivar_medico(id_medico):
            flash("Médico reactivado correctamente", "success")
        else:
            flash("Error al reactivar el médico", "danger")
    except Exception as e:
        flash(f"Error al reactivar médico: {str(e)}", "danger")
    return redirect(url_for('admin_medicos_eliminados'))

# Ruta para consultar médico (ver detalles)
@app.route("/admin/consultar-medico/<int:id_medico>")
@requiere_rol([1])  # Solo admin
def admin_consultar_medico(id_medico):
    try:
        medico = MedicoController.obtener_medico_por_id(id_medico)
        if not medico:
            flash("Médico no encontrado", "warning")
            return redirect(url_for('home'))
        
        return render_template('admin/consultar_medico.html',
                             medico=medico,
                             tipo_usuario=session.get('tipo_usuario', ''))
                             
    except Exception as e:
        flash(f"Error al cargar médico: {str(e)}", "danger")
        return redirect(url_for('home'))
    
# Rutas temporales
@app.route("/debug-medico/<int:id_medico>")
@requiere_rol([1])
def debug_medico(id_medico):
    """Ruta temporal para diagnosticar el problema"""
    try:
        print(f"=== DEBUG MÉDICO ID: {id_medico} ===")
        
        # 1. Verificar en la tabla usuarios
        query_usuarios = "SELECT * FROM r4l.usuarios WHERE id_medico = ?"
        resultado_usuarios = Database.execute_query(query_usuarios, (id_medico,))
        usuario = resultado_usuarios[0] if resultado_usuarios else None
        print(f"Usuario encontrado: {usuario}")
        
        # 2. Verificar en la tabla medico_personal
        query_personal = "SELECT * FROM r4l.medico_personal WHERE id_medico = ?"
        resultado_personal = Database.execute_query(query_personal, (id_medico,))
        personal = resultado_personal[0] if resultado_personal else None
        print(f"Personal encontrado: {personal}")
        
        # 3. Verificar la consulta completa
        query_completa = """
            SELECT u.id_medico, u.username, mp.nombres, mp.apellido_paterno
            FROM r4l.usuarios u
            INNER JOIN r4l.medico_personal mp ON u.id_medico = mp.id_medico
            WHERE u.id_medico = ?
        """
        resultado_completo = Database.execute_query(query_completa, (id_medico,))
        completo = resultado_completo[0] if resultado_completo else None
        print(f"Consulta completa: {completo}")
        
        return f"""
        <h1>Debug Médico ID: {id_medico}</h1>
        <h3>Tabla usuarios:</h3>
        <pre>{usuario}</pre>
        <h3>Tabla medico_personal:</h3>
        <pre>{personal}</pre>
        <h3>Consulta JOIN:</h3>
        <pre>{completo}</pre>
        """
        
    except Exception as e:
        return f"Error en debug: {str(e)}"

@app.route("/test-medico/<int:id_medico>")
@requiere_rol([1])
def test_medico(id_medico):
    """Ruta simple para testear la búsqueda de médico"""
    try:
        medico = MedicoController.obtener_medico_por_id(id_medico)
        if medico:
            return f"""
            <h1>Médico Encontrado</h1>
            <p>ID: {medico[0]}</p>
            <p>Nombre: {medico[8]} {medico[9]} {medico[10] or ''}</p>
            <p>Usuario: {medico[4]}</p>
            <p>Email: {medico[5]}</p>
            """
        else:
            return f"<h1>Médico con ID {id_medico} NO encontrado</h1>"
    except Exception as e:
        return f"Error: {str(e)}"
    
@app.route('/debug-tablas-detalle')
def debug_tablas_detalle():
    try:
        conn = Config(0)
        cursor = conn.cursor()
        
        # Obtener todas las tablas con más detalle
        cursor.execute("""
            SELECT 
                TABLE_SCHEMA,
                TABLE_NAME,
                TABLE_TYPE
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_TYPE = 'BASE TABLE'
            ORDER BY TABLE_NAME
        """)
        tablas = cursor.fetchall()
        
        resultado = "<h2>Tablas en la base de datos:</h2><ul>"
        for schema, nombre, tipo in tablas:
            resultado += f"<li>Esquema: {schema} - Tabla: {nombre} - Tipo: {tipo}</li>"
        resultado += "</ul>"
        
        # También verificar si hay tablas que contengan 'sexo' en el nombre
        cursor.execute("""
            SELECT TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME LIKE '%sexo%'
        """)
        tablas_sexo = cursor.fetchall()
        
        resultado += "<h2>Tablas que contienen 'sexo':</h2><ul>"
        for tabla in tablas_sexo:
            resultado += f"<li>{tabla[0]}</li>"
        resultado += "</ul>"
        
        cursor.close()
        conn.close()
        
        return resultado
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(port=3000, debug=True)