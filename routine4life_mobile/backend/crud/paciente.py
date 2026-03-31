# routine4life_mobile/backend/crud/paciente.py
from sqlalchemy.orm import Session
from shared import models 
from routine4life_mobile.backend.schemas import paciente as schemas
from datetime import date, datetime
import bcrypt

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

def obtener_historial_consultas(db: Session, id_paciente: int):
    return db.query(models.consultas_medicas)\
             .filter(models.consultas_medicas.id_paciente == id_paciente)\
             .order_by(models.consultas_medicas.fecha.desc())\
             .all()
             
def obtener_sintomas_paciente(db: Session, id_paciente: int):
    return db.query(models.sintomas_consulta)\
             .join(models.consultas_medicas, models.consultas_medicas.id_consulta == models.sintomas_consulta.id_consulta)\
             .filter(models.consultas_medicas.id_paciente == id_paciente)\
             .all()
             
def obtener_recetas_paciente(db: Session, id_paciente: int):
    # Puente: Recetas -> Consultas -> Paciente
    return db.query(models.recetas_medicas)\
             .join(models.consultas_medicas, models.consultas_medicas.id_consulta == models.recetas_medicas.id_consulta)\
             .filter(models.consultas_medicas.id_paciente == id_paciente)\
             .order_by(models.recetas_medicas.fecha.desc())\
             .all()
             
def obtener_medicamentos_paciente(db: Session, id_paciente: int):
    return db.query(models.medicamentos_recetados)\
             .join(models.recetas_medicas, models.recetas_medicas.id_receta == models.medicamentos_recetados.id_receta)\
             .join(models.consultas_medicas, models.consultas_medicas.id_consulta == models.recetas_medicas.id_consulta)\
             .filter(models.consultas_medicas.id_paciente == id_paciente)\
             .all()
             
def obtener_rutinas_paciente(db: Session, id_paciente: int):
    return db.query(models.rutinas_recetadas)\
             .join(models.recetas_medicas, models.recetas_medicas.id_receta == models.rutinas_recetadas.id_receta)\
             .join(models.consultas_medicas, models.consultas_medicas.id_consulta == models.recetas_medicas.id_consulta)\
             .filter(models.consultas_medicas.id_paciente == id_paciente)\
             .all()
             
def crear_registro_paciente(db: Session, registro: schemas.RegistroPacienteCreate):
    nuevo_registro = models.registros_paciente(
        id_paciente=registro.id_paciente,
        id_tipo_registro=registro.id_tipo_registro,
        fecha=registro.fecha,
        hora=registro.hora,
        valor=registro.valor,
        unidad_alternativa=registro.unidad_alternativa,
        notas=registro.notas
    )
    
    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro) 
    
    return nuevo_registro

def obtener_hash_contrasena(contrasena: str):
    contrasena_bytes = contrasena.encode('utf-8')
    hash_bytes = bcrypt.hashpw(contrasena_bytes, bcrypt.gensalt())
    return hash_bytes.decode('utf-8')

def crear_credenciales_usuario(db: Session, usuario: schemas.UsuarioCreate):
    nuevo_usuario = models.usuarios(
        id_rol=usuario.id_rol,
        id_medico=usuario.id_medico,
        id_paciente=usuario.id_paciente,
        contrasena=obtener_hash_contrasena(usuario.contrasena),
        fecha_registro=date.today() 
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return nuevo_usuario

def verificar_contrasena(contrasena_plana: str, contrasena_hash: str):
    return bcrypt.checkpw(
        contrasena_plana.encode('utf-8'), 
        contrasena_hash.encode('utf-8')
    )

def autenticar_paciente(db: Session, credenciales: schemas.LoginRequest):
    usuario = db.query(models.usuarios)\
                .join(models.pacientes_aplicacion, models.pacientes_aplicacion.id_paciente == models.usuarios.id_paciente)\
                .filter(models.pacientes_aplicacion.email == credenciales.email)\
                .first()
    
    if not usuario:
        return None
        
    if not verificar_contrasena(credenciales.contrasena, usuario.contrasena):
        return None
        
    return usuario

# NUEVA FUNCIÓN PARA ACTUALIZAR CONTRASEÑA
def actualizar_contrasena_paciente(db: Session, datos: schemas.RestablecerContrasenaRequest):
    usuario = db.query(models.usuarios)\
                .join(models.pacientes_aplicacion, models.pacientes_aplicacion.id_paciente == models.usuarios.id_paciente)\
                .filter(models.pacientes_aplicacion.email == datos.email)\
                .first()
    
    if not usuario:
        return False
        
    usuario.contrasena = obtener_hash_contrasena(datos.nueva_contrasena)
    db.commit()
    db.refresh(usuario)
    
    return True