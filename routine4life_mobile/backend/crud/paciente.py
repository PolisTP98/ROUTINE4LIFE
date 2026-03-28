# routine4life_mobile/backend/crud/paciente.py
from sqlalchemy.orm import Session
from shared import models 
from routine4life_mobile.backend.schemas import paciente as schemas
from datetime import date, datetime

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

def obtener_diagnostico_paciente(db: Session, id_paciente: int):
    return db.query(models.tipos_diabetes)\
             .join(models.pacientes)\
             .filter(models.pacientes.id_paciente == id_paciente)\
             .first()
             
def obtener_medico_de_paciente(db: Session, id_paciente: int):
    
    return db.query(models.datos_personales_medico)\
             .join(models.medicos, models.medicos.id_medico == models.datos_personales_medico.id_medico)\
             .join(models.consultas_medicas, models.consultas_medicas.id_medico == models.medicos.id_medico)\
             .filter(models.consultas_medicas.id_paciente == id_paciente)\
             .first() 
             
def obtener_horarios_medico(db: Session, id_medico: int):
    return db.query(models.horarios_medicos)\
             .filter(
                 models.horarios_medicos.id_medico == id_medico,
                 models.horarios_medicos.activo == True
             )\
             .all()
             
def crear_cita_medica(db: Session, cita: schemas.CitaCreate):
    nueva_cita = models.citas_medicas(
        id_rol=cita.id_rol,
        id_medico=cita.id_medico,
        id_paciente=cita.id_paciente,
        id_estatus_cita=cita.id_estatus_cita,
        fecha=cita.fecha,
        hora=cita.hora,
        motivo=cita.motivo,
        notas=cita.notas,
        fecha_hora_solicitud=datetime.now() 
    )
    
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita) 
    
    return nueva_cita