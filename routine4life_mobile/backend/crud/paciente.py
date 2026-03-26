# routine4life_mobile/backend/crud/paciente.py
from sqlalchemy.orm import Session
from shared import models 
from routine4life_mobile.backend.schemas import paciente as schemas
from datetime import date

def registrar_cuenta_movil(db: Session, registro: schemas.RegistroAppCreate):
    db_registro_app = models.pacientes_aplicacion(
        id_paciente=registro.id_paciente,
        id_sexo=registro.id_sexo,
        id_pais=registro.id_pais,
        id_estatus_usuario=registro.id_estatus_usuario,
        nombre_completo=registro.nombre_completo,
        fecha_nacimiento=registro.fecha_nacimiento,
        email=registro.email,
        telefono=registro.telefono,
        fecha_registro=date.today() 
    )
    db.add(db_registro_app)
    db.commit()
    db.refresh(db_registro_app)
    return db_registro_app