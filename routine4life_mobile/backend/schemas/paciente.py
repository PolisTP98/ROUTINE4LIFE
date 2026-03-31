# routine4life_mobile/backend/schemas/paciente.py
from pydantic import BaseModel
from datetime import date, time, datetime
from typing import List, Optional
from decimal import Decimal


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
        
class ConsultaMedicaResponse(BaseModel):
    id_consulta: int
    id_cita: int
    id_medico: int
    fecha: date
    hora: time
    peso: Optional[Decimal] = None
    altura: Optional[int] = None
    presion_sistolica: Optional[int] = None
    presion_diastolica: Optional[int] = None
    frecuencia_cardiaca: Optional[int] = None
    glucosa_ayunas: Optional[Decimal] = None
    glucosa_postprandial: Optional[Decimal] = None
    hemoglobina_glicosilada: Optional[Decimal] = None
    colesterol_total: Optional[Decimal] = None
    trigliceridos: Optional[Decimal] = None
    nivel_insulina: Optional[Decimal] = None
    notas: Optional[str] = None
    plan_tratamiento: Optional[str] = None

    class Config:
        from_attributes = True
        
class SintomaConsultaResponse(BaseModel):
    id_sintoma: int
    id_consulta: int
    id_sintoma_diabetes: int
    intensidad: Optional[int] = None
    duracion: Optional[str] = None
    notas: Optional[str] = None

    class Config:
        from_attributes = True
        
class RecetaMedicaResponse(BaseModel):
    id_receta: int
    id_consulta: int
    fecha: date
    hora: time
    instrucciones_generales: Optional[str] = None
    url_pdf: Optional[str] = None

    class Config:
        from_attributes = True
        
class MedicamentoRecetadoResponse(BaseModel):
    id_medicamento: int
    id_receta: int
    id_medicamento_diabetes: int
    dosis: str
    frecuencia: str
    duracion: Optional[str] = None
    instrucciones_adicionales: Optional[str] = None

    class Config:
        from_attributes = True
        
class RutinaRecetadaResponse(BaseModel):
    id_rutina: int
    id_receta: int
    id_tipo_rutina: int
    id_comida: Optional[int] = None
    descripcion: str
    frecuencia: Optional[str] = None
    duracion: Optional[str] = None
    notas: Optional[str] = None

    class Config:
        from_attributes = True
        
class RegistroPacienteCreate(BaseModel):
    id_paciente: int
    id_tipo_registro: int 
    fecha: date
    hora: time
    valor: Decimal
    unidad_alternativa: Optional[str] = None
    notas: Optional[str] = None

class RegistroPacienteResponse(RegistroPacienteCreate):
    id_registro: int

    class Config:
        from_attributes = True
        
class UsuarioCreate(BaseModel):
    id_rol: int
    id_paciente: Optional[int] = None
    id_medico: Optional[int] = None
    contrasena: str
    
class UsuarioResponse(BaseModel):
    id_usuario: int
    id_rol: int
    id_paciente: Optional[int] = None
    id_medico: Optional[int] = None
    fecha_registro: date

    class Config:
        from_attributes = True
        
# ... (Tu código anterior)

class LoginRequest(BaseModel):
    email: str
    contrasena: str

class LoginResponse(BaseModel):
    mensaje: str
    id_usuario: int
    id_paciente: Optional[int] = None
    id_rol: int

    class Config:
        from_attributes = True