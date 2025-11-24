from config import config
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
import pyodbc

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.before_request
def session_temporal():
    session.permanent = False

def connectDB(
        SERVER = 'POLISTP98', 
        DRIVER = 'ODBC Driver 18 for SQL Server', 
        DATABASE = 'ROUTINE4LIFE_DB', 
        Trusted_Connection = True,
        Encrypt = True, 
        TrustServerCertificate = True):
    
    connection = config(DRIVER, SERVER, DATABASE, Trusted_Connection, Encrypt, TrustServerCertificate)
    return connection

# Ruta de login
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['id_user']
        password = request.form['password']
        
        # Validación simple - en producción usaría autenticación real
        if username and password:
            session['user'] = username
            flash("Login exitoso", "success")
            return redirect(url_for('home'))
        else:
            flash("Por favor ingrese usuario y contraseña", "danger")
    
    return render_template('login.html')

@app.route("/home")
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    try:
        conn = connectDB()
        cursor = conn.cursor()
        
        # Consulta de ejemplo - ajusta según tu esquema de base de datos
        cursor.execute("SELECT TOP 10 * FROM INFORMATION_SCHEMA.TABLES")
        tablas = cursor.fetchall()
        
        conn.close()
        return render_template('home.html', tablas=tablas, usuario=session['user'])
    
    except Exception as e:
        return f"Error al conectar con la base de datos: {e}"

@app.route("/logout")
def logout():
    session.pop('user', None)
    flash("Sesión cerrada exitosamente", "info")
    return redirect(url_for('login'))

# Ruta para verificar conexión a BD
@app.route("/dbcheck")
def dbcheck():
    try:
        conn = connectDB()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        conn.close()
        return jsonify({"status": "OK", "message": "Conexión exitosa a la base de datos"})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(port=3000, debug=True)