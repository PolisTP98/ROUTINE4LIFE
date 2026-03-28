# miAPI/models/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

# ==================== MÉDICOS ====================
class MedicoBase(BaseModel):
    nombre_completo: str
    email: EmailStr
    rfc: str
    cedula_profesional: str
    codigo: str
    id_especialidad: int
    id_sexo: int
    fecha_nacimiento: date
    telefono: str

class MedicoCreate(MedicoBase):
    contrasena: str

class MedicoUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    email: Optional[EmailStr] = None
    rfc: Optional[str] = None
    cedula_profesional: Optional[str] = None
    id_especialidad: Optional[int] = None
    telefono: Optional[str] = None
    id_estatus_usuario: Optional[int] = None

class MedicoResponse(BaseModel):
    id_medico: int
    nombre_completo: str
    email: str
    especialidad: str
    activo: bool

# ==================== PACIENTES ====================
class PacienteBase(BaseModel):
    nombre_completo: str
    fecha_nacimiento: date
    id_sexo: int
    id_tipo_diabetes: Optional[int] = None

class PacienteCreate(PacienteBase):
    id_medico: int

class PacienteUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    id_sexo: Optional[int] = None
    id_tipo_diabetes: Optional[int] = None
    id_estatus_usuario: Optional[int] = None

class PacienteResponse(BaseModel):
    id_paciente: int
    nombre_completo: str
    fecha_nacimiento: date
    edad: int
    sexo: str
    tipo_diabetes: Optional[str]
    codigo: str
    medico_nombre: Optional[str]