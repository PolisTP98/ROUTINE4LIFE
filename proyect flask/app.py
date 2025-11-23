from flask import Flask
import pyodbc

app = Flask(__name__)

@app.route("/")
def probar_conexion():
    configuraciones = [
        # Probemos diferentes configuraciones
        "DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-6RRSB8S\\SQLEXPRESS01;DATABASE=ROUTINE4LIFE_DB;Trusted_Connection=yes;",
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6RRSB8S\\SQLEXPRESS01;DATABASE=ROUTINE4LIFE_DB;Trusted_Connection=yes;",
        "DRIVER={SQL Server Native Client 11.0};SERVER=DESKTOP-6RRSB8S\\SQLEXPRESS01;DATABASE=ROUTINE4LIFE_DB;Trusted_Connection=yes;",
        "DRIVER={SQL Server};SERVER=DESKTOP-6RRSB8S\\SQLEXPRESS01;DATABASE=ROUTINE4LIFE_DB;Trusted_Connection=yes;"
    ]
    
    resultados = []
    
    for i, config in enumerate(configuraciones):
        try:
            conn = pyodbc.connect(config)
            cursor = conn.cursor()
            
            # Verificar BD
            cursor.execute("SELECT DB_NAME()")
            db_name = cursor.fetchone()[0]
            
            # Verificar tablas
            cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'r4l'")
            tablas_count = cursor.fetchone()[0]
            
            # Verificar médicos
            cursor.execute("SELECT COUNT(*) FROM r4l.medico_personal")
            medicos_count = cursor.fetchone()[0]
            
            cursor.close()
            conn.close()
            
            resultados.append(f"CONEXION {i}: EXITOSA")
            resultados.append(f"  - Base de datos: {db_name}")
            resultados.append(f"  - Tablas en r4l: {tablas_count}")
            resultados.append(f"  - Médicos en BD: {medicos_count}")
            resultados.append("")
            
        except Exception as e:
            resultados.append(f"CONEXION {i}: FALLIDA")
            resultados.append(f"  - Error: {str(e)}")
            resultados.append("")
    
    html = "<h1>Prueba de Conexión a ROUTINE4LIFE_DB</h1>"
    html += "<pre>" + "\n".join(resultados) + "</pre>"
    
    # Si alguna conexión funcionó, mostrar opción de login
    if any("EXITOSA" in r for r in resultados):
        html += '<h2><a href="/login">Probar Login con Médicos</a></h2>'
    
    return html

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        rfc = request.form.get("rfc", "").strip()
        
        try:
            # Usar la primera configuración que funcione
            conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6RRSB8S\\SQLEXPRESS01;DATABASE=ROUTINE4LIFE_DB;Trusted_Connection=yes;")
            cursor = conn.cursor()
            
            cursor.execute("SELECT id_medico, rfc, nombres, apellido_paterno FROM r4l.medico_personal WHERE rfc = ?", rfc)
            medico = cursor.fetchone()
            
            cursor.close()
            conn.close()
            
            if medico:
                return f"""
                <h1>Médico Encontrado en ROUTINE4LIFE_DB</h1>
                <p><strong>ID:</strong> {medico[0]}</p>
                <p><strong>RFC:</strong> {medico[1]}</p>
                <p><strong>Nombre:</strong> {medico[2]} {medico[3]}</p>
                <br>
                <a href="/login">Buscar otro médico</a>
                """
            else:
                return f"""
                <h1>Médico No Encontrado</h1>
                <p>No existe médico con RFC: {rfc} en la BD</p>
                <a href="/login">Intentar con otro RFC</a>
                """
                
        except Exception as e:
            return f"Error de conexión: {str(e)}"
    
    return """
    <h1>Login - Buscar Médico en ROUTINE4LIFE_DB</h1>
    <form method="POST">
        <input type="text" name="rfc" placeholder="RFC del médico" required>
        <button type="submit">Buscar en BD</button>
    </form>
    <p>Ejemplo: PERE800101ABC</p>
    """

if __name__ == "__main__":
    from flask import request
    app.run(port=3000, debug=True)