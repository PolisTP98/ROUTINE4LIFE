from flask import request, session, flash, redirect, url_for
from models.database import Database
from functools import wraps

class AuthController:
    @staticmethod
    def login():
        if request.method == 'POST':
            username = request.form['id_user']
            password = request.form['password']
            
            if username and password:
                try:
                    print(f"DEBUG: Usuario intentando login: {username}")
                    
                    # Consulta CORREGIDA - incluir id_rol e id_medico
                    user_data = Database.execute_query("""
                        SELECT 
                            u.username, 
                            u.contrasena_cifrada, 
                            m.nombres, 
                            m.apellido_paterno,
                            u.id_estatus,
                            u.id_rol,  -- AÑADIR esto
                            m.id_medico  -- AÑADIR esto
                        FROM r4l.usuarios u
                        INNER JOIN r4l.medico_personal m ON u.id_medico = m.id_medico
                        WHERE u.username = ? AND u.id_estatus = 1
                    """, (username,))
                    
                    if user_data:
                        # CORREGIR la asignación de variables
                        username_db, contrasena_cifrada_db, nombres, apellidos, id_estatus, id_rol, id_medico = user_data[0]
                        print(f"DEBUG: Usuario encontrado: {username_db}")
                        print(f"DEBUG: Rol del usuario: {id_rol}")
                        print(f"DEBUG: ID Médico: {id_medico}")
                        print(f"DEBUG: Contraseña en BD: '{contrasena_cifrada_db}'")
                        print(f"DEBUG: Contraseña ingresada: '{password}'")
                        
                        # Comparación directa
                        if password == contrasena_cifrada_db:
                            # GUARDAR TODOS los datos en sesión
                            session['user'] = username
                            session['nombre_completo'] = f"{nombres} {apellidos}"
                            session['id_rol'] = id_rol  # ¡IMPORTANTE!
                            session['id_medico'] = id_medico
                            
                            # Determinar tipo de usuario
                            if id_rol == 1:  # Médico administrador
                                session['tipo_usuario'] = 'admin'
                                flash("Bienvenido Administrador", "success")
                            elif id_rol == 2:  # Médico normal
                                session['tipo_usuario'] = 'medico'
                                flash("Bienvenido Doctor", "success")
                            else:  # Paciente u otro
                                session['tipo_usuario'] = 'usuario'
                                flash("Bienvenido", "success")
                            
                            # Forzar guardado de sesión
                            session.modified = True
                            print(f"DEBUG: Sesión después del login: {dict(session)}")
                            print("DEBUG: Login EXITOSO - Redirigiendo a home")
                            return True
                        else:
                            flash("Contraseña incorrecta", "danger")
                            print("DEBUG: Contraseña NO coincide")
                            return False
                    else:
                        flash("Usuario no encontrado o inactivo", "danger")
                        print("DEBUG: Usuario no encontrado en BD")
                    
                except Exception as e:
                    print(f"DEBUG: Error durante login: {str(e)}")
                    import traceback
                    print(f"DEBUG: Traceback completo: {traceback.format_exc()}")
                    flash(f"Error de conexión: {str(e)}", "danger")
            else:
                flash("Por favor ingrese usuario y contraseña", "danger")
        
        return False

def requiere_rol(roles_permitidos):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print(f"DEBUG: Verificando acceso a {f.__name__}")
            print(f"DEBUG: Sesión actual: {dict(session)}")
            
            if 'id_rol' not in session:
                print("DEBUG: No hay id_rol en sesión - redirigiendo a login")
                flash("Debe iniciar sesión", "danger")
                return redirect(url_for('login'))
            
            if session['id_rol'] not in roles_permitidos:
                print(f"DEBUG: Rol {session['id_rol']} no permitido. Permitidos: {roles_permitidos}")
                flash("No tiene permisos para acceder a esta página", "danger")
                return redirect(url_for('home'))
            
            print(f"DEBUG: Acceso permitido para rol {session['id_rol']}")
            return f(*args, **kwargs)
        return decorated_function
    return decorator