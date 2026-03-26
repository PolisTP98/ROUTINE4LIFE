# routine4life_mobile/backend/routers/pacientes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from shared.database import get_db
from routine4life_mobile.backend.schemas import paciente as schemas
from routine4life_mobile.backend.crud import paciente as crud

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