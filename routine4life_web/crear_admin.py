import sys
from pathlib import Path
from sqlalchemy import text
import bcrypt
import random

# 🔥 IMPORTANTE: esto va ANTES del import
sys.path.append(str(Path(__file__).resolve().parent.parent))

from shared.database import SessionLocal


def crear_admin():
    db = SessionLocal()
    email_admin = 'admin@routine4life.com'
    password_plana = 'admin123'

    password_hasheada = bcrypt.hashpw(
        password_plana.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

    try:
        # 🔍 Verificar si ya existe
        id_usuario_existente = db.execute(text("""
            SELECT u.id_usuario 
            FROM r4l.usuarios u
            JOIN r4l.medicos m ON u.id_medico = m.id_medico
            WHERE m.email = :email
        """), {"email": email_admin}).scalar()

        if id_usuario_existente:
            print("El administrador ya existe. Actualizando contraseña...")
            db.execute(text("""
                UPDATE r4l.usuarios 
                SET contrasena = :pass_hash 
                WHERE id_usuario = :id_u
            """), {"pass_hash": password_hasheada, "id_u": id_usuario_existente})
            db.commit()
            print("✅ Contraseña actualizada.")
            return

        print("🚀 Creando nuevo administrador...")

        # 🔥 GENERAR DATOS ÚNICOS (AQUÍ ESTABA TU ERROR)
        telefono = str(random.randint(1000000, 9999999))
        rfc = f"ADMIN{random.randint(1000,9999)}"
        codigo = f"ADMIN-{random.randint(100,999)}"

        print("TEL GENERADO:", telefono)

        # 🔒 Desactivar triggers
        db.execute(text("DISABLE TRIGGER utg_auditorias_medicos ON r4l.medicos"))
        db.execute(text("DISABLE TRIGGER utg_auditorias_usuarios ON r4l.usuarios"))
        db.commit()

        # 1️⃣ Insertar datos personales
        db.execute(text("""
            INSERT INTO r4l.datos_personales_medico
            (id_sexo, id_pais, nombre_completo, fecha_nacimiento, telefono, fecha_hora_registro)
            VALUES (1, 1, 'Administrador Sistema', '1990-01-01', :telefono, GETDATE())
        """), {"telefono": telefono})
        db.commit()

        # 2️⃣ Obtener ID con el TELÉFONO NUEVO
        id_medico = db.execute(text("""
            SELECT id_medico 
            FROM r4l.datos_personales_medico 
            WHERE telefono = :telefono
        """), {"telefono": telefono}).scalar()

        print(f"✅ ID médico generado: {id_medico}")

        # 3️⃣ Insertar médico (SIN valores fijos)
        db.execute(text("""
            INSERT INTO r4l.medicos
            (id_medico, id_rol, id_especialidad, id_estatus_usuario,
            codigo, cedula_profesional, email, rfc)
            VALUES (:id, 1, 1, 1, :codigo, :rfc, :email, :rfc)
        """), {
            "id": id_medico,
            "codigo": codigo,
            "rfc": rfc,
            "email": email_admin
        })
        db.commit()

        # 4️⃣ Insertar usuario
        db.execute(text("""
            INSERT INTO r4l.usuarios
            (id_rol, id_medico, id_paciente, contrasena, fecha_registro)
            VALUES (1, :id, NULL, :pass_hash, GETDATE())
        """), {
            "id": id_medico,
            "pass_hash": password_hasheada
        })
        db.commit()

        print("🎉 Administrador creado correctamente")
        print(f"📧 Email: {email_admin}")
        print(f"🔑 Password: {password_plana}")

    except Exception as e:
        db.rollback()
        print(f"❌ Error al crear administrador: {e}")

    finally:
        try:
            db.execute(text("ENABLE TRIGGER utg_auditorias_medicos ON r4l.medicos"))
            db.execute(text("ENABLE TRIGGER utg_auditorias_usuarios ON r4l.usuarios"))
            db.commit()
        except:
            pass

        db.close()


if __name__ == "__main__":
    crear_admin()
