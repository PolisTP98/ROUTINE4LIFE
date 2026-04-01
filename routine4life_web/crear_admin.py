import sys
import os
from pathlib import Path
from sqlalchemy import text
from werkzeug.security import generate_password_hash 

sys.path.append(str(Path(__file__).parent))

from shared.database import SessionLocal

def crear_admin():
    db = SessionLocal()
    email_admin = 'admin@routine4life.com'
    password_plana = 'admin123'
    
    password_hasheada = generate_password_hash(password_plana)

    try:
        id_usuario_existente = db.execute(text("""
            SELECT u.id_usuario FROM r4l.usuarios u
            JOIN r4l.medicos m ON u.id_medico = m.id_medico
            WHERE m.email = :email
        """), {"email": email_admin}).scalar()

        if id_usuario_existente:
            print(f"El administrador ya existe. Actualizando contraseña al formato hash...")
            db.execute(text("""
                UPDATE r4l.usuarios 
                SET contrasena = :pass_hash 
                WHERE id_usuario = :id_u
            """), {"pass_hash": password_hasheada, "id_u": id_usuario_existente})
            db.commit()
            print("Contraseña actualizada exitosamente. Ya puedes iniciar sesión.")
            return

        print("Creando nuevo administrador desde cero...")
        
        # Deshabilitar triggers temporalmente para evitar errores de auditoría
        db.execute(text("DISABLE TRIGGER utg_auditorias_medicos ON r4l.medicos"))
        db.execute(text("DISABLE TRIGGER utg_auditorias_usuarios ON r4l.usuarios"))
        db.commit()

        # 1. Insertar datos personales
        db.execute(text("""
            INSERT INTO r4l.datos_personales_medico
            (id_sexo, id_pais, nombre_completo, fecha_nacimiento, telefono, fecha_hora_registro)
            VALUES (1, 1, 'Administrador Sistema', '1990-01-01', '555554', GETDATE())
        """))
        db.commit()

        # 2. Obtener el id generado
        id_medico = db.execute(text("""
            SELECT id_medico FROM r4l.datos_personales_medico 
            WHERE telefono = '555554'
        """)).scalar()

        print(f"ID médico generado: {id_medico}")

        # 3. Insertar médico
        db.execute(text("""
            INSERT INTO r4l.medicos
            (id_medico, id_rol, id_especialidad, id_estatus_usuario,
            codigo, cedula_profesional, email, rfc)
            VALUES (:id, 1, 1, 1, 'ADMIN-001', 'ADMIN001', :email, 'ADMIN001')
        """), {"id": id_medico, "email": email_admin})
        db.commit()

        # 4. Insertar usuario con la contraseña HASHEADA
        db.execute(text("""
            INSERT INTO r4l.usuarios
            (id_rol, id_medico, id_paciente, contrasena, fecha_registro)
            VALUES (1, :id, NULL, :pass_hash, GETDATE())
        """), {"id": id_medico, "pass_hash": password_hasheada})
        db.commit()

        # Rehabilitar triggers
        db.execute(text("ENABLE TRIGGER utg_auditorias_medicos ON r4l.medicos"))
        db.execute(text("ENABLE TRIGGER utg_auditorias_usuarios ON r4l.usuarios"))
        db.commit()

        print("Administrador creado exitosamente con contraseña encriptada.")
        print(f"Email: {email_admin}")
        print(f"Contraseña: {password_plana}")

    except Exception as e:
        db.rollback()
        try:
            db.execute(text("ENABLE TRIGGER utg_auditorias_medicos ON r4l.medicos"))
            db.execute(text("ENABLE TRIGGER utg_auditorias_usuarios ON r4l.usuarios"))
            db.commit()
        except:
            pass
        print(f"Error al crear administrador: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    crear_admin()