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