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

# Ruta para login con mejor manejo de errores
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
    
    try:
        id_rol = session.get('id_rol')
        
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
        
        else:  # Médico normal - mostrar pacientes
            pacientes = PacienteController.obtener_pacientes()
            return render_template('medico/dashboard_medico.html',
                                 pacientes=pacientes,
                                 usuario=session['user'],
                                 nombre_completo=session.get('nombre_completo', ''),
                                 tipo_usuario=session.get('tipo_usuario', ''))
    
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
    try:
        Database.execute_query("SELECT 1")
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

# Ruta para que admin agregue médicos
@app.route("/admin/agregar-medico", methods=['GET', 'POST'])
@requiere_rol([1])  # Solo admin
def admin_agregar_medico():  # CAMBIA el nombre de la función
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
            
            MedicoController.agregar_medico(datos)
            flash("Médico agregado exitosamente", "success")
            return redirect(url_for('home'))
            
        except Exception as e:
            flash(f"Error al agregar médico: {str(e)}", "danger")
    
    sexos = PacienteController.obtener_sexos()
    paises = PacienteController.obtener_paises()
    documentos = MedicoController.obtener_documentos_legales()
    
    return render_template('admin/agregar_medico.html',
                         sexos=sexos,
                         paises=paises,
                         documentos=documentos,
                         tipo_usuario=session.get('tipo_usuario', ''))
    
# Ruta para agregar paciente con manejo de errores completo
@app.route("/medico/agregar-paciente", methods=['GET', 'POST'])
@requiere_rol([1, 2])
def medico_agregar_paciente():
    if request.method == 'POST':
        try:
            # Validaciones exhaustivas
            errores = []
            
            # Validar nombres
            nombres = request.form.get('nombres', '').strip()
            if not nombres:
                errores.append("El nombre es obligatorio")
            elif len(nombres) > 200:
                errores.append("El nombre no puede tener más de 200 caracteres")
            
            # Validar apellido paterno
            apellido_paterno = request.form.get('apellido_paterno', '').strip()
            if not apellido_paterno:
                errores.append("El apellido paterno es obligatorio")
            elif len(apellido_paterno) > 100:
                errores.append("El apellido paterno no puede tener más de 100 caracteres")
            
            # Validar apellido materno
            apellido_materno = request.form.get('apellido_materno', '').strip()
            if apellido_materno and len(apellido_materno) > 100:
                errores.append("El apellido materno no puede tener más de 100 caracteres")
            
            # Validar fecha de nacimiento
            fecha_nacimiento = request.form.get('fecha_nacimiento', '')
            if not fecha_nacimiento:
                errores.append("La fecha de nacimiento es obligatoria")
            else:
                # Validar que la fecha sea válida y no sea futura
                from datetime import datetime
                try:
                    fecha_obj = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
                    if fecha_obj > datetime.now():
                        errores.append("La fecha de nacimiento no puede ser futura")
                except ValueError:
                    errores.append("La fecha de nacimiento no tiene un formato válido")
            
            # Validar sexo
            id_sexo = request.form.get('id_sexo', '')
            if not id_sexo:
                errores.append("El sexo es obligatorio")
            elif not id_sexo.isdigit():
                errores.append("El sexo seleccionado no es válido")
            
            # Validar país
            id_pais = request.form.get('id_pais', '')
            if not id_pais:
                errores.append("El país es obligatorio")
            elif not id_pais.isdigit():
                errores.append("El país seleccionado no es válido")
            
            # Si hay errores, mostrarlos todos
            if errores:
                for error in errores:
                    flash(error, "danger")
                return redirect(url_for('medico_agregar_paciente'))
            
            # Si pasa todas las validaciones, proceder
            datos = {
                'id_sexo': int(id_sexo),
                'id_pais': int(id_pais),
                'nombres': nombres,
                'apellido_paterno': apellido_paterno,
                'apellido_materno': apellido_materno,
                'fecha_nacimiento': fecha_nacimiento
            }
            
            PacienteController.agregar_paciente(datos)
            flash("Paciente agregado exitosamente", "success")
            return redirect(url_for('home'))
            
        except Exception as e:
            print(f"ERROR CRÍTICO en agregar_paciente: {str(e)}")
            flash("Error interno del sistema al agregar paciente. Por favor, intente nuevamente.", "danger")
            return redirect(url_for('medico_agregar_paciente'))
    
    # GET - Mostrar formulario
    try:
        sexos = PacienteController.obtener_sexos()
        paises = PacienteController.obtener_paises()
        
        return render_template('medico/agregar_paciente.html',
                             sexos=sexos,
                             paises=paises,
                             tipo_usuario=session.get('tipo_usuario', ''))
    except Exception as e:
        print(f"ERROR cargando formulario: {str(e)}")
        flash("Error al cargar el formulario", "danger")
        return redirect(url_for('home'))
    
@app.route("/medico/lista-pacientes")
@requiere_rol([1, 2])  # Admin y médicos normales
def medico_lista_pacientes():  # CAMBIA el nombre de la función
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
        
# Ruta para editar paciente con manejo de errores
@app.route("/medico/editar-paciente/<int:id_paciente>", methods=['GET', 'POST'])
@requiere_rol([1, 2])
def editar_paciente(id_paciente):
    if request.method == 'POST':
        try:
            # Validaciones (similar a agregar paciente)
            errores = []
            
            nombres = request.form.get('nombres', '').strip()
            if not nombres:
                errores.append("El nombre es obligatorio")
            
            apellido_paterno = request.form.get('apellido_paterno', '').strip()
            if not apellido_paterno:
                errores.append("El apellido paterno es obligatorio")
            
            fecha_nacimiento = request.form.get('fecha_nacimiento', '')
            if not fecha_nacimiento:
                errores.append("La fecha de nacimiento es obligatoria")
            
            id_sexo = request.form.get('id_sexo', '')
            if not id_sexo:
                errores.append("El sexo es obligatorio")
            
            id_pais = request.form.get('id_pais', '')
            if not id_pais:
                errores.append("El país es obligatorio")
            
            if errores:
                for error in errores:
                    flash(error, "danger")
                return redirect(url_for('editar_paciente', id_paciente=id_paciente))
            
            datos = {
                'id_sexo': int(id_sexo),
                'id_pais': int(id_pais),
                'nombres': nombres,
                'apellido_paterno': apellido_paterno,
                'apellido_materno': request.form.get('apellido_materno', '').strip(),
                'fecha_nacimiento': fecha_nacimiento
            }
            
            PacienteController.actualizar_paciente(id_paciente, datos)
            flash("Paciente actualizado correctamente", "success")
            return redirect(url_for('home'))
            
        except Exception as e:
            print(f"ERROR actualizando paciente {id_paciente}: {str(e)}")
            flash("Error al actualizar el paciente", "danger")
            return redirect(url_for('editar_paciente', id_paciente=id_paciente))
    
    # GET - Mostrar formulario de edición
    try:
        paciente = PacienteController.obtener_paciente_por_id(id_paciente)
        if not paciente:
            flash("Paciente no encontrado o ha sido eliminado", "warning")
            return redirect(url_for('home'))
        
        sexos = PacienteController.obtener_sexos()
        paises = PacienteController.obtener_paises()
        
        return render_template('medico/editar_paciente.html',
                             paciente=paciente,
                             sexos=sexos,
                             paises=paises,
                             tipo_usuario=session.get('tipo_usuario', ''))
                             
    except Exception as e:
        print(f"ERROR cargando edición paciente {id_paciente}: {str(e)}")
        flash("Error al cargar el paciente para editar", "danger")
        return redirect(url_for('home'))
        
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
    print(f"=== DEBUG EDITAR MÉDICO - INICIO ===")
    print(f"ID médico recibido: {id_medico}")
    print(f"Tipo de ID: {type(id_medico)}")
    print(f"Usuario en sesión: {session.get('user')}")
    print(f"Rol en sesión: {session.get('id_rol')}")
    
    if request.method == 'POST':
        print("=== MÉTODO POST DETECTADO ===")
        try:
            datos = {
                'id_rol': int(request.form['id_rol']),
                'id_sexo': int(request.form['id_sexo']),
                'id_pais': int(request.form['id_pais']),
                'id_documento': int(request.form['id_documento']),
                'numero_identificacion': request.form['numero_identificacion'],
                'nombres': request.form['nombres'],
                'apellido_paterno': request.form['apellido_paterno'],
                'apellido_materno': request.form.get('apellido_materno', ''),
                'fecha_nacimiento': request.form['fecha_nacimiento'],
                'telefono': request.form['telefono'],
                'email_personal': request.form['email_personal'],
                'email_laboral': request.form['email_laboral'],
                'rfc': request.form.get('rfc', ''),
                'direccion': request.form.get('direccion', '')
            }
            
            print(f"DEBUG: Datos del formulario: {datos}")
            
            if MedicoController.actualizar_medico(id_medico, datos):
                print("DEBUG: Médico actualizado exitosamente")
                flash("Médico actualizado exitosamente", "success")
            else:
                print("DEBUG: Error al actualizar el médico")
                flash("Error al actualizar el médico", "danger")
                
            return redirect(url_for('home'))
            
        except Exception as e:
            print(f"DEBUG: Error en POST: {str(e)}")
            import traceback
            traceback.print_exc()
            flash(f"Error al actualizar médico: {str(e)}", "danger")
            return redirect(url_for('admin_editar_medico', id_medico=id_medico))
    
    # GET - Mostrar formulario de edición
    print("=== MÉTODO GET - BUSCANDO MÉDICO ===")
    try:
        print(f"DEBUG: Llamando a obtener_medico_por_id({id_medico})")
        medico = MedicoController.obtener_medico_por_id(id_medico)
        print(f"DEBUG: Resultado de obtener_medico_por_id: {medico}")
        
        if not medico:
            print("DEBUG: Médico NO encontrado - redirigiendo a home con flash")
            flash("Médico no encontrado", "warning")
            return redirect(url_for('home'))
        
        print("DEBUG: Médico ENCONTRADO - obteniendo datos para dropdowns")
        
        # Obtener sexos
        print("DEBUG: Obteniendo sexos...")
        sexos = PacienteController.obtener_sexos()
        print(f"DEBUG: Sexos obtenidos: {sexos}")
        
        # Obtener países
        print("DEBUG: Obteniendo países...")
        paises = PacienteController.obtener_paises()
        print(f"DEBUG: Países obtenidos: {paises}")
        
        # Obtener documentos
        print("DEBUG: Obteniendo documentos...")
        documentos = MedicoController.obtener_documentos_legales()
        print(f"DEBUG: Documentos obtenidos: {documentos}")
        
        # Obtener roles
        print("DEBUG: Obteniendo roles...")
        roles = MedicoController.obtener_roles()
        print(f"DEBUG: Roles obtenidos: {roles}")
        
        print("DEBUG: Todos los datos obtenidos - renderizando template")
        
        return render_template('admin/editar_medico.html',
                             medico=medico,
                             sexos=sexos,
                             paises=paises,
                             documentos=documentos,
                             roles=roles,
                             tipo_usuario=session.get('tipo_usuario', ''))
                             
    except Exception as e:
        print(f"DEBUG: Error EXCEPCIÓN en editar médico: {str(e)}")
        import traceback
        traceback.print_exc()
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
if __name__ == "__main__":
    app.run(port=3000, debug=True)