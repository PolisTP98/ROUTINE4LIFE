# routine4life_mobile/backend/schemas/paciente.py
from pydantic import BaseModel
from datetime import date

class PacienteCreate(BaseModel):
    id_sexo: int
    id_estatus_usuario: int
    codigo: str
    nombre_completo: str
    fecha_nacimiento: date

class PacienteResponse(PacienteCreate):
    id_paciente: int

    class Config:
        from_attributes = True