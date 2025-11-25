from config import Config
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import pyodbc

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.before_request
def session_temporal():
    session.permanent = False

# Ruta de login CORREGIDA
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['id_user']
        password = request.form['password']
        
        if username and password:
            conn = None
            cursor = None
            try:
                print(f"DEBUG: Intentando login para usuario: {username}")
                
                # Obtener la conexión directamente
                conn = Config(0)  # Esto devuelve la conexión, no el objeto DatabaseConnection
                cursor = conn.cursor()
                
                # Consulta simple para verificar la conexión primero
                cursor.execute("SELECT 1 as test")
                test_result = cursor.fetchone()
                print(f"DEBUG: Conexión a BD exitosa: {test_result[0]}")
                
                # Buscar tabla de usuarios
                cursor.execute("""
                    SELECT TABLE_NAME 
                    FROM INFORMATION_SCHEMA.TABLES 
                    WHERE TABLE_TYPE = 'BASE TABLE'
                """)
                todas_tablas = cursor.fetchall()
                print("DEBUG: Tablas disponibles:")
                for tabla in todas_tablas:
                    print(f"   - {tabla[0]}")
                
                # Buscar específicamente tabla de usuarios
                tabla_usuarios = None
                for nombre in ['usuarios', 'users', 'user', 'Usuarios', 'Users']:
                    cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ?", nombre)
                    if cursor.fetchone()[0] > 0:
                        tabla_usuarios = nombre
                        break
                
                if tabla_usuarios:
                    print(f"DEBUG: Tabla de usuarios encontrada: {tabla_usuarios}")
                    
                    # Ver las columnas de esta tabla
                    cursor.execute("""
                        SELECT COLUMN_NAME 
                        FROM INFORMATION_SCHEMA.COLUMNS 
                        WHERE TABLE_NAME = ?
                    """, tabla_usuarios)
                    columnas = [col[0] for col in cursor.fetchall()]
                    print(f"DEBUG: Columnas: {columnas}")
                    
                    # Intentar diferentes combinaciones de columnas
                    combinaciones = [
                        ('id_user', 'password'),
                        ('usuario', 'contrasena'),
                        ('username', 'password'),
                        ('email', 'password'),
                        ('user_id', 'user_password')
                    ]
                    
                    usuario_valido = False
                    for user_col, pass_col in combinaciones:
                        if user_col in columnas and pass_col in columnas:
                            try:
                                cursor.execute(f"SELECT * FROM {tabla_usuarios} WHERE {user_col} = ? AND {pass_col} = ?", 
                                             (username, password))
                                if cursor.fetchone():
                                    usuario_valido = True
                                    break
                            except:
                                continue
                    
                    if usuario_valido:
                        session['user'] = username
                        flash("Login exitoso", "success")
                        return redirect(url_for('home'))
                    else:
                        flash("Usuario o contraseña incorrectos", "danger")
                else:
                    print("DEBUG: No se encontró tabla de usuarios")
                    # Simular login exitoso para testing (ELIMINAR EN PRODUCCIÓN)
                    session['user'] = username
                    flash("Login exitoso (modo prueba)", "success")
                    return redirect(url_for('home'))
                
            except Exception as e:
                print(f"DEBUG: Error durante login: {str(e)}")
                import traceback
                print(f"DEBUG: Traceback: {traceback.format_exc()}")
                flash(f"Error de conexión: {str(e)}", "danger")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
        else:
            flash("Por favor ingrese usuario y contraseña", "danger")
    
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
        
        # Consulta simple de tablas
        cursor.execute("SELECT TOP 10 TABLE_NAME, TABLE_TYPE FROM INFORMATION_SCHEMA.TABLES")
        tablas = cursor.fetchall()
        print(f"DEBUG: Se encontraron {len(tablas)} tablas")
        
        return render_template('home.html', tablas=tablas, usuario=session['user'])
    
    except Exception as e:
        print(f"DEBUG: Error en home: {str(e)}")
        return f"Error al cargar la página: {str(e)}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/logout")
def logout():
    session.pop('user', None)
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
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(port=3000, debug=True)