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
if __name__ == "__main__":
    app.run(port=3000, debug=True)