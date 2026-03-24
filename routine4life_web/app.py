from flask import Flask, render_template

app = Flask(__name__)

# Login
@app.route("/")
def login():
    return render_template("login.html")


# registro
@app.route("/registro")
def registro():
    return render_template("registro.html")


# Recuperar contraseña
@app.route("/recuperar")
def recuperar_contrasena():
    return render_template("recuperar_contrasena.html")


# Datos clinicos del paciente
@app.route("/datos_clinicos")
def datos_clinicos():
    return render_template("datos_clinicos.html")


# Detalles del paciente
@app.route("/detalle_paciente")
def detalle_paciente():
    return render_template("detalle_paciente.html")


# Historial de consultas
@app.route("/historial_consulta")
def historial_consulta():
    return render_template("historial_consulta.html")


# Detalle de sintomas
@app.route("/sintomas")
def sintomas():
    return render_template("sintomas_detalle.html")


# Tratamiento del paciente
@app.route("/tratamiento")
def tratamiento():
    return render_template("tratamiento_paciente.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)