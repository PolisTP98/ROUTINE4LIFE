# ---------------------------------------------------------------------
# | IMPORTAR LOS MÓDULOS DE TODAS LAS TABLAS (CATÁLOGO Y PRINCIPALES) |
# ---------------------------------------------------------------------

# IMPORTAR MODELOS CATÁLOGO
from .catalogues import(
    Sexos, RolesUsuarios, EstatusUsuarios, Continentes,
    Paises, DocumentosLegales, Sucursales, Departamentos,
    TiposContratos, Especialidades, Comidas
)

# IMPORTAR MODELOS PRINCIPALES
from .main import(
    MedicoPersonal, MedicoLaboral, EspecialidadesMedico,
    Pacientes, CitaPaciente, RutinaEjercicio, RutinaAlimentacion,
    DescripcionRutina, PacientesAplicacion, UsuariosPacientes
)

# LISTA COMPLETA DE TODOS LOS MODELOS PARA SQLAlchemy
__all__ = [

    # MODELOS CATÁLOGO
    'Sexos',
    'RolesUsuarios',
    'EstatusUsuarios',
    'Continentes',
    'Paises',
    'DocumentosLegales',
    'Sucursales',
    'Departamentos',
    'TiposContratos',
    'Especialidades',
    'Comidas',
    
    # MODELOS PRINCIPALES
    'MedicoPersonal',
    'MedicoLaboral',
    'EspecialidadesMedico',
    'Pacientes',
    'CitaPaciente',
    'RutinaEjercicio',
    'RutinaAlimentacion',
    'DescripcionRutina',
    'PacientesAplicacion',
    'UsuariosPacientes'
]

# DICCIONARIO PARA ACCESO RÁPIDO AL MODELO ORM POR EL NOMBRE DE LA TABLA
MODELOS_POR_TABLA = {

    # MODELOS CATÁLOGO
    'sexos': Sexos,
    'roles_usuarios': RolesUsuarios,
    'estatus_usuarios': EstatusUsuarios,
    'continentes': Continentes,
    'paises': Paises,
    'documentos_legales': DocumentosLegales,
    'sucursales': Sucursales,
    'departamentos': Departamentos,
    'tipos_contratos': TiposContratos,
    'especialidades': Especialidades,
    'comidas': Comidas,
    
    # MODELOS PRINCIPALES
    'medico_personal': MedicoPersonal,
    'medico_laboral': MedicoLaboral,
    'especialidades_medico': EspecialidadesMedico,
    'pacientes': Pacientes,
    'cita_paciente': CitaPaciente,
    'rutina_ejercicio': RutinaEjercicio,
    'rutina_alimentacion': RutinaAlimentacion,
    'descripcion_rutina': DescripcionRutina,
    'pacientes_aplicacion': PacientesAplicacion,
    'usuarios_pacientes': UsuariosPacientes
}