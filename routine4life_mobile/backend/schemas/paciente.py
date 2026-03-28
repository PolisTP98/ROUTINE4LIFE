# routine4life_mobile/backend/schemas/paciente.py
from pydantic import BaseModel
from datetime import date, time, datetime
from typing import List
from typing import Optional

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
        
class TipoDiabetesResponse(BaseModel):
    id_tipo_diabetes: int
    nombre: str

    class Config:
        from_attributes = True
        
class MedicoAsignadoResponse(BaseModel):
    id_medico: int
    nombre_completo: str
    telefono: str

    class Config:
        from_attributes = True
        
class HorarioMedicoResponse(BaseModel):
    id_horario: int
    dia_semana: int
    hora_inicio: time
    hora_fin: time

    class Config:
        from_attributes = True
        
class CitaCreate(BaseModel):
    id_rol: int             
    id_medico: int          
    id_paciente: int         
    id_estatus_cita: int = 1 
    fecha: date
    hora: time
    motivo: Optional[str] = None
    notas: Optional[str] = None

class CitaResponse(CitaCreate):
    id_cita: int
    fecha_hora_solicitud: datetime

    class Config:
        from_attributes = True