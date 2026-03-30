import sys
import os
from pathlib import Path

# Agregar el path para importar shared/database.py
sys.path.append(str(Path(__file__).parent))

from sqlalchemy import text
from shared.database import SessionLocal

def crear_admin():
    db = SessionLocal()
    try:
        # Verificar si ya existe el admin
        existe = db.execute(text("""
            SELECT COUNT(*) FROM r4l.usuarios 
            WHERE id_medico IN (
                SELECT id_medico FROM r4l.medicos 
                WHERE email = 'admin@routine4life.com'
            )
        """)).scalar()

        if existe > 0:
            print("El administrador ya existe en la BD.")
            return

        # Deshabilitar triggers temporalmente
        db.execute(text("DISABLE TRIGGER utg_auditorias_medicos ON r4l.medicos"))
        db.execute(text("DISABLE TRIGGER utg_auditorias_usuarios ON r4l.usuarios"))
        db.commit()

        # 1. Insertar datos personales
        db.execute(text("""
            INSERT INTO r4l.datos_personales_medico 
            (id_sexo, id_pais, nombre_completo, fecha_nacimiento, telefono, fecha_hora_registro)
            VALUES (1, 1, 'Administrador Sistema', '1990-01-01', '5599999999', GETDATE())
        """))
        db.commit()

        # 2. Obtener el id generado
        id_medico = db.execute(text("""
            SELECT id_medico FROM r4l.datos_personales_medico 
            WHERE telefono = '5599999999'
        """)).scalar()

        print(f"ID médico generado: {id_medico}")

        # 3. Insertar médico
        db.execute(text(f"""
            INSERT INTO r4l.medicos 
            (id_medico, id_rol, id_especialidad, id_estatus_usuario, 
            codigo, cedula_profesional, email, rfc)
            VALUES ({id_medico}, 1, 1, 1, 
            'ADMIN-001', 'ADMIN001', 'admin@routine4life.com', 'ADMIN001')
        """))
        db.commit()

        # 4. Insertar usuario
        db.execute(text(f"""
            INSERT INTO r4l.usuarios 
            (id_rol, id_medico, id_paciente, contrasena, fecha_registro)
            VALUES (1, {id_medico}, NULL, 'admin123', GETDATE())
        """))
        db.commit()

        # Rehabilitar triggers
        db.execute(text("ENABLE TRIGGER utg_auditorias_medicos ON r4l.medicos"))
        db.execute(text("ENABLE TRIGGER utg_auditorias_usuarios ON r4l.usuarios"))
        db.commit()

        print("Administrador creado exitosamente.")
        print("Email:      admin@routine4life.com")
        print("Contraseña: admin123")

    except Exception as e:
        db.rollback()
        # Intentar rehabilitar triggers aunque haya error
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