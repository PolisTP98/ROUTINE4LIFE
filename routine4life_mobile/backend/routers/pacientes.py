# routine4life_mobile/backend/routers/pacientes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.database import get_db
from routine4life_mobile.backend.schemas import paciente as schemas
from routine4life_mobile.backend.crud import paciente as crud

router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes (App Móvil)"]
)

@router.post("/", response_model=schemas.PacienteResponse)
def registrar_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.create_paciente(db=db, paciente=paciente)

@router.get("/{paciente_id}", response_model=schemas.PacienteResponse)
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente(db, paciente_id=paciente_id)
    if not db_paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente