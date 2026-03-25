# routine4life_mobile/backend/crud/paciente.py
from sqlalchemy.orm import Session
from shared import models # Importamos desde la carpeta compartida
from routine4life_mobile.backend.schemas import paciente as schemas
from datetime import datetime

def get_paciente(db: Session, paciente_id: int):
    return db.query(models.pacientes).filter(models.pacientes.id_paciente == paciente_id).first()

def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_paciente = models.pacientes(
        id_sexo=paciente.id_sexo,
        id_estatus_usuario=paciente.id_estatus_usuario,
        codigo=paciente.codigo,
        nombre_completo=paciente.nombre_completo,
        fecha_nacimiento=paciente.fecha_nacimiento,
        fecha_hora_registro=datetime.now()
    )
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente