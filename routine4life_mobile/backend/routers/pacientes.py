# routine4life_mobile/backend/routers/pacientes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from shared.database import get_db
from routine4life_mobile.backend.schemas import paciente as schemas
from routine4life_mobile.backend.crud import paciente as crud
from typing import List

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
        db.rollback() # Protegemos la base de datos si algo sale mal
        raise HTTPException(
            status_code=400, 
            detail=f"Error al guardar el registro. Verifica que el paciente y el tipo de registro existan. Detalle: {str(e)}"
        )
        
@router.post("/crear-cuenta", response_model=schemas.UsuarioResponse)
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # 1. Validar que no manden todo vacío
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