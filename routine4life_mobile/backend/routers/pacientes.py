# routine4life_mobile/backend/routers/pacientes.py
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy import func, cast, Date
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from shared.database import get_db
from routine4life_mobile.backend.schemas import paciente as schemas
from routine4life_mobile.backend.crud import paciente as crud
from typing import List
from shared import models
from datetime import datetime
from werkzeug.security import check_password_hash


router = APIRouter(
    prefix="/auth-movil", 
    tags=["Registro y Autenticación (App Móvil)"]
)

@router.post("/registro", response_model=schemas.RegistroAppResponse)
def crear_cuenta_paciente(registro: schemas.RegistroAppCreate, db: Session = Depends(get_db)):
    try:
        return crud.registrar_cuenta_movil(db=db, registro=registro)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="Error de validación: Verifica que el ID del paciente exista y que el email/teléfono no estén duplicados."
        )
        
@router.get("/{id_paciente}/diagnostico", response_model=schemas.TipoDiabetesResponse)
def obtener_tipo_diabetes(id_paciente: int, db: Session = Depends(get_db)):
    diagnostico = crud.obtener_diagnostico_paciente(db=db, id_paciente=id_paciente)
    
    if not diagnostico:
        raise HTTPException(
            status_code=404, 
            detail="No se encontró un diagnóstico de diabetes para este paciente o el paciente no existe."
        )
        
    return diagnostico

@router.get("/{id_paciente}/medico", response_model=schemas.MedicoAsignadoResponse)
def obtener_medico_asignado(id_paciente: int, db: Session = Depends(get_db)):
    medico = crud.obtener_medico_de_paciente(db=db, id_paciente=id_paciente)
    
    if not medico:
        raise HTTPException(
            status_code=404, 
            detail="No se encontró un médico asignado para este paciente o el paciente no existe."
        )
        
    return medico

@router.get("/medico/{id_medico}/horarios", response_model=List[schemas.HorarioMedicoResponse])
def obtener_horarios_disponibles(id_medico: int, db: Session = Depends(get_db)):
    horarios = crud.obtener_horarios_medico(db=db, id_medico=id_medico)
    
    if not horarios:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron horarios activos disponibles para este médico."
        )
        
    return horarios

@router.get("/sexos", response_model=List[schemas.SexoResponse])
def obtener_lista_sexos(db: Session = Depends(get_db)):
    sexos = crud.obtener_sexos(db=db)
    
    if not sexos:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron registros de sexo en la base de datos."
        )
        
    return sexos

@router.post("/citas", response_model=schemas.CitaResponse)
def agendar_cita(cita: schemas.CitaCreate, db: Session = Depends(get_db)):
    try:
        nueva_cita = crud.crear_cita_medica(db=db, cita=cita)
        return nueva_cita
    except Exception as e:
        db.rollback() 
        raise HTTPException(
            status_code=400, 
            detail=f"Error al agendar la cita. Verifica que los IDs existan. Detalle: {str(e)}"
        )
        
@router.get("/{id_paciente}/consultas", response_model=List[schemas.ConsultaMedicaResponse])
def obtener_consultas_paciente(id_paciente: int, db: Session = Depends(get_db)):
    consultas = crud.obtener_historial_consultas(db=db, id_paciente=id_paciente)
    
    if not consultas:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron consultas médicas en el historial de este paciente."
        )
        
    return consultas

@router.get("/{id_paciente}/sintomas", response_model=List[schemas.SintomaConsultaResponse])
def obtener_sintomas_diagnosticados(id_paciente: int, db: Session = Depends(get_db)):
    sintomas = crud.obtener_sintomas_paciente(db=db, id_paciente=id_paciente)
    
    if not sintomas:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron síntomas registrados en las consultas de este paciente."
        )
        
    return sintomas

@router.get("/{id_paciente}/recetas", response_model=List[schemas.RecetaMedicaResponse])
def obtener_recetas_emitidas(id_paciente: int, db: Session = Depends(get_db)):
    recetas = crud.obtener_recetas_paciente(db=db, id_paciente=id_paciente)
    
    if not recetas:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron recetas médicas en el historial de este paciente."
        )
        
    return recetas

@router.get("/{id_paciente}/medicamentos", response_model=List[schemas.MedicamentoRecetadoResponse])
def obtener_medicamentos_recetados(id_paciente: int, db: Session = Depends(get_db)):
    medicamentos = crud.obtener_medicamentos_paciente(db=db, id_paciente=id_paciente)
    
    if not medicamentos:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron medicamentos recetados en el historial de este paciente."
        )
        
    return medicamentos

@router.get("/{id_paciente}/rutinas", response_model=List[schemas.RutinaRecetadaResponse])
def obtener_rutinas_recetadas(id_paciente: int, db: Session = Depends(get_db)):
    rutinas = crud.obtener_rutinas_paciente(db=db, id_paciente=id_paciente)
    
    if not rutinas:
        raise HTTPException(
            status_code=404, 
            detail="No se encontraron rutinas recetadas en el historial de este paciente."
        )
        
    return rutinas

@router.post("/registros", response_model=schemas.RegistroPacienteResponse)
def guardar_registro_medico(registro: schemas.RegistroPacienteCreate, db: Session = Depends(get_db)):
    try:
        nuevo_registro = crud.crear_registro_paciente(db=db, registro=registro)
        return nuevo_registro
    except Exception as e:
        db.rollback() 
        raise HTTPException(
            status_code=400, 
            detail=f"Error al guardar el registro. Verifica que el paciente y el tipo de registro existan. Detalle: {str(e)}"
        )
        
@router.post("/crear-cuenta", response_model=schemas.UsuarioResponse)
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    if not usuario.id_paciente and not usuario.id_medico:
        raise HTTPException(
            status_code=400, 
            detail="Debes proporcionar el id_paciente o el id_medico para vincular la cuenta."
        )
        
    try:
        nuevo_usuario = crud.crear_credenciales_usuario(db=db, usuario=usuario)
        return nuevo_usuario
        
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="Error: Este paciente o médico ya tiene una cuenta registrada, o los IDs proporcionados no existen."
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


@router.get("/buscar-paciente")
def buscar_paciente(nombre: str, fecha: str, db: Session = Depends(get_db)):

    # 🔹 Limpiar datos del frontend
    nombre = nombre.strip().lower()

    try:
        fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
    except:
        raise HTTPException(status_code=400, detail="Formato de fecha inválido (YYYY-MM-DD)")

    print("NOMBRE FRONT:", nombre)
    print("FECHA FRONT:", fecha)

    paciente = db.query(models.pacientes).filter(
        func.lower(func.trim(models.pacientes.nombre_completo)).like(f"%{nombre}%"),
        cast(models.pacientes.fecha_nacimiento, Date) == fecha
    ).first()

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    return {
        "id_paciente": paciente.id_paciente,
        "nombre_completo": paciente.nombre_completo,
        "fecha_nacimiento": str(paciente.fecha_nacimiento)
    }
    
    
from fastapi import Body
import bcrypt

@router.post("/login")
def login(data: dict = Body(...), db: Session = Depends(get_db)):

    email = data.get("email")
    contrasena = data.get("contrasena")

    if not email or not contrasena:
        raise HTTPException(status_code=400, detail="Email y contraseña requeridos")

    # Buscar directamente en pacientes_aplicacion
    paciente = db.query(models.pacientes_aplicacion).filter(
        models.pacientes_aplicacion.email == email
    ).first()
    
    if not paciente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Buscar el usuario asociado para la contraseña
    usuario = db.query(models.usuarios).filter(
        models.usuarios.id_paciente == paciente.id_paciente
    ).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Credenciales no encontradas")

    # Verificar contraseña
    if not check_password_hash(usuario.contrasena, contrasena):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    return {
        "mensaje": "Login exitoso",
        "id_usuario": usuario.id_usuario,
        "id_paciente": paciente.id_paciente,
        "nombre_completo": paciente.nombre_completo
    }
    
@router.post("/registro-completo")
def registro_completo(data: schemas.RegistroCompletoCreate, db: Session = Depends(get_db)):
    """
    Registro completo para pacientes que ya existen en el sistema web.
    Crea automáticamente pacientes_aplicacion y usuarios en un solo paso.
    """
    from werkzeug.security import generate_password_hash
    from datetime import date
    
    id_paciente = data.id_paciente
    email = data.email
    telefono = data.telefono
    contrasena = data.contrasena
    nombre_completo = data.nombre_completo
    fecha_nacimiento_str = data.fecha_nacimiento
    
    # Validaciones
    if not all([id_paciente, email, telefono, contrasena]):
        raise HTTPException(
            status_code=400, 
            detail="Faltan datos: id_paciente, email, telefono y contrasena son requeridos"
        )
    
    # Verificar que el paciente existe en tabla pacientes
    paciente = db.query(models.pacientes).filter(
        models.pacientes.id_paciente == id_paciente
    ).first()
    
    if not paciente:
        raise HTTPException(
            status_code=404, 
            detail="Paciente no encontrado en el sistema. Contacta a tu médico."
        )
    
    # Validar fecha si viene
    if fecha_nacimiento_str:
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        except:
            fecha_nacimiento = paciente.fecha_nacimiento
    else:
        fecha_nacimiento = paciente.fecha_nacimiento
    
    # Usar nombre del paciente si no se proporcionó
    if not nombre_completo:
        nombre_completo = paciente.nombre_completo
    
    # 1. Crear o actualizar en pacientes_aplicacion
    paciente_app = db.query(models.pacientes_aplicacion).filter(
        models.pacientes_aplicacion.id_paciente == id_paciente
    ).first()
    
    if not paciente_app:
        paciente_app = models.pacientes_aplicacion(
            id_paciente=id_paciente,
            id_sexo=paciente.id_sexo,
            id_pais=1,
            id_estatus_usuario=1,
            nombre_completo=nombre_completo,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            telefono=telefono,
            fecha_registro=date.today()
        )
        db.add(paciente_app)
        db.flush()
        mensaje_app = "Creado registro en aplicación"
    else:
        # Actualizar email y teléfono si ya existía
        paciente_app.email = email
        paciente_app.telefono = telefono
        db.flush()
        mensaje_app = "Actualizado registro existente"
    
    # 2. Verificar si ya tiene credenciales
    usuario_existente = db.query(models.usuarios).filter(
        models.usuarios.id_paciente == id_paciente
    ).first()
    
    if usuario_existente:
        # Actualizar contraseña
        usuario_existente.contrasena = generate_password_hash(contrasena)
        mensaje_pass = "Contraseña actualizada"
    else:
        # Crear nuevas credenciales
        nuevo_usuario = models.usuarios(
            id_rol=3,  # Paciente
            id_paciente=id_paciente,
            contrasena=generate_password_hash(contrasena),
            fecha_registro=date.today()
        )
        db.add(nuevo_usuario)
        mensaje_pass = "Credenciales creadas"
    
    db.commit()
    
    return {
        "mensaje": "Registro completado exitosamente",
        "detalle": f"{mensaje_app}, {mensaje_pass}",
        "id_paciente": id_paciente,
        "email": email
    }