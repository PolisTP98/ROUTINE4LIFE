# ----------------------------------------------
# | IMPORTAR LOS MÓDULOS DE TABLAS PRINCIPALES |
# ----------------------------------------------

from .medico_personal import MedicoPersonal
from .medico_laboral import MedicoLaboral
from .especialidades_medico import EspecialidadesMedico
from .pacientes import Pacientes
from .cita_paciente import CitaPaciente
from .rutina_ejercicio import RutinaEjercicio
from .rutina_alimentacion import RutinaAlimentacion
from .descripcion_rutina import DescripcionRutina
from .pacientes_aplicacion import PacientesAplicacion
from .usuarios_pacientes import UsuariosPacientes


# ----------------------------------------------------
# | LISTA CON TODAS LAS TABLAS BAJO EL ESQUEMA "r4l" |
# ----------------------------------------------------

__all__ = [
    "MedicoPersonal", 
    "MedicoLaboral", 
    "EspecialidadesMedico", 
    "Pacientes", 
    "CitaPaciente", 
    "RutinaEjercicio", 
    "RutinaAlimentacion", 
    "DescripcionRutina", 
    "PacientesAplicacion", 
    "UsuariosPacientes"
]