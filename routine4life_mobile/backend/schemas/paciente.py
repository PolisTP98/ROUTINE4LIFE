# routine4life_mobile/backend/schemas/paciente.py
from pydantic import BaseModel
from datetime import date

class RegistroAppCreate(BaseModel):
    id_paciente: int  
    id_sexo: int
    id_pais: int
    id_estatus_usuario: int
    nombre_completo: str
    fecha_nacimiento: date
    email: str
    telefono: str

class RegistroAppResponse(RegistroAppCreate):
    fecha_registro: date

    class Config:
        from_attributes = True