# -------------------------------------------
# | IMPORTAR TODOS LOS MÓDULOS DE CATÁLOGOS |
# -------------------------------------------

from .sexos import Sexos
from .roles_usuarios import RolesUsuarios
from .estatus_usuarios import EstatusUsuarios
from .continentes import Continentes
from .paises import Paises
from .documentos_legales import DocumentosLegales
from .sucursales import Sucursales
from .departamentos import Departamentos
from .tipos_contratos import TiposContratos
from .especialidades import Especialidades
from .comidas import Comidas


# ----------------------------------------------------
# | LISTA CON TODAS LAS TABLAS BAJO EL ESQUEMA "r4l" |
# ----------------------------------------------------

__all__ = [
    "Sexos", 
    "RolesUsuarios", 
    "EstatusUsuarios", 
    "Continentes", 
    "Paises", 
    "DocumentosLegales", 
    "Sucursales", 
    "Departamentos", 
    "TiposContratos", 
    "Especialidades", 
    "Comidas"
]