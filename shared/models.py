# ----------------------------
# | IMPORTACIONES NECESARIAS |
# ----------------------------

from sqlalchemy import (
    Column, Integer, String, Date, DateTime, Time, Numeric, 
    SmallInteger, Boolean, Text, ForeignKey, Index
)
from sqlalchemy.orm import relationship
from shared.database import Base


# -----------------------------------------
# | MODELOS ORM - TABLAS DE TIPO CATÁLOGO |
# -----------------------------------------

# r4l.sexos
class sexos(Base):
    __tablename__ = "sexos"
    __table_args__ = {"schema": "r4l"}

    id_sexo = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL SEXO")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DEL SEXO")

    # RELACIÓN: sexos -> datos_personales_medico (1:N)
    datos_personales_medico = relationship("datos_personales_medico", back_populates = "sexo")
    # RELACIÓN: sexos -> pacientes (1:N)
    pacientes = relationship("pacientes", back_populates = "sexo")
    # RELACIÓN: sexos -> pacientes_aplicacion (1:N)
    pacientes_aplicacion = relationship("pacientes_aplicacion", back_populates = "sexo")

# r4l.continentes
class continentes(Base):
    __tablename__ = "continentes"
    __table_args__ = {"schema": "r4l"}

    id_continente = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL CONTINENTE")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DEL CONTINENTE")

    # RELACIÓN: continentes -> paises (1:N)
    paises = relationship("paises", back_populates = "continente", cascade = "all, delete-orphan")

# r4l.paises
class paises(Base):
    __tablename__ = "paises"
    __table_args__ = (
        Index("ix_paises_id_continente", "id_continente"), 
        {"schema": "r4l"}
    )

    id_pais = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL PAÍS")
    id_continente = Column(Integer, ForeignKey("r4l.continentes.id_continente"), nullable = False, comment = "IDENTIFICADOR DEL CONTINENTE AL QUE PERTENECE (FK)")
    nombre = Column(String(50), nullable = False, unique = True, comment = "NOMBRE DEL PAÍS")
    codigo_iso = Column(String(3), nullable = False, unique = True, comment = "CÓDIGO ISO DE TRES LETRAS")
    codigo_telefonico = Column(String(6), nullable = False, comment = "PREFIJO TELEFÓNICO DEL PAÍS (INCLUYE '+')")

    # RELACIÓN: paises -> continentes (N:1)
    continente = relationship("continentes", back_populates = "paises")
    # RELACIÓN: paises -> datos_personales_medico (1:N)
    datos_personales_medico = relationship("datos_personales_medico", back_populates = "pais")
    # RELACIÓN: paises -> pacientes_aplicacion (1:N)
    pacientes_aplicacion = relationship("pacientes_aplicacion", back_populates = "pais")

# r4l.comidas
class comidas(Base):
    __tablename__ = "comidas"
    __table_args__ = {"schema": "r4l"}

    id_comida = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA COMIDA")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DE LA COMIDA")

    # RELACIÓN: comidas -> rutinas_recetadas (1:N)
    rutinas_recetadas = relationship("rutinas_recetadas", back_populates = "comida")

# r4l.roles_usuarios
class roles_usuarios(Base):
    __tablename__ = "roles_usuarios"
    __table_args__ = {"schema": "r4l"}

    id_rol = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL ROL")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DEL ROL")

    # RELACIÓN: roles_usuarios -> medicos (1:N)
    medicos = relationship("medicos", back_populates = "rol")
    # RELACIÓN: roles_usuarios -> citas_medicas (1:N)
    citas = relationship("citas_medicas", back_populates = "rol")
    # RELACIÓN: roles_usuarios -> usuarios (1:N)
    usuarios = relationship("usuarios", back_populates = "rol")

# r4l.estatus_usuarios
class estatus_usuarios(Base):
    __tablename__ = "estatus_usuarios"
    __table_args__ = {"schema": "r4l"}

    id_estatus_usuario = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL ESTATUS DEL USUARIO")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DEL ESTATUS DEL USUARIO")
    descripcion = Column(String(100), nullable = True, comment = "DESCRIPCIÓN DETALLADA")

    # RELACIÓN: estatus_usuarios -> medicos (1:N)
    medicos = relationship("medicos", back_populates = "estatus")
    # RELACIÓN: estatus_usuarios -> pacientes (1:N)
    pacientes = relationship("pacientes", back_populates = "estatus")
    # RELACIÓN: estatus_usuarios -> pacientes_aplicacion (1:N)
    pacientes_aplicacion = relationship("pacientes_aplicacion", back_populates = "estatus")

# r4l.sucursales_hospitalarias
class sucursales_hospitalarias(Base):
    __tablename__ = "sucursales_hospitalarias"
    __table_args__ = {"schema": "r4l"}

    id_sucursal = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA SUCURSAL")
    codigo = Column(String(20), nullable = False, unique = True, comment = "CÓDIGO DE LA SUCURSAL")
    nombre = Column(String(50), nullable = False, comment = "NOMBRE DE LA SUCURSAL")
    url_ubicacion = Column(String(255), nullable = False, comment = "URL DE LA UBICACIÓN (GOOGLE MAPS, ETC.)")

# r4l.presentaciones_medicamentos
class presentaciones_medicamentos(Base):
    __tablename__ = "presentaciones_medicamentos"
    __table_args__ = {"schema": "r4l"}

    id_presentacion = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA PRESENTACIÓN")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DE LA PRESENTACIÓN")

    # RELACIÓN: presentaciones_medicamentos -> medicamentos_diabetes (1:N)
    medicamentos_diabetes = relationship("medicamentos_diabetes", back_populates = "presentacion")

# r4l.unidades_medida
class unidades_medida(Base):
    __tablename__ = "unidades_medida"
    __table_args__ = {"schema": "r4l"}

    id_unidad = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA UNIDAD")
    nombre = Column(String(10), nullable = False, unique = True, comment = "NOMBRE DE LA UNIDAD")

    # RELACIÓN: unidades_medida -> medicamentos_diabetes (1:N)
    medicamentos_diabetes = relationship("medicamentos_diabetes", back_populates = "unidad")
    # RELACIÓN: unidades_medida -> tipos_registros (1:N)
    tipos_registros = relationship("tipos_registros", back_populates = "unidad")

# r4l.tipos_diabetes
class tipos_diabetes(Base):
    __tablename__ = "tipos_diabetes"
    __table_args__ = {"schema": "r4l"}

    id_tipo_diabetes = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL TIPO DE DIABETES")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DEL TIPO DE DIABETES")

    # RELACIÓN: tipos_diabetes -> pacientes (1:N)
    pacientes = relationship("pacientes", back_populates = "tipo_diabetes")

# r4l.sintomas_diabetes
class sintomas_diabetes(Base):
    __tablename__ = "sintomas_diabetes"
    __table_args__ = {"schema": "r4l"}

    id_sintoma_diabetes = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL SÍNTOMA")
    nombre = Column(String(50), nullable = False, unique = True, comment = "NOMBRE DEL SÍNTOMA")
    descripcion = Column(String(255), nullable = True, comment = "DESCRIPCIÓN DETALLADA")

    # RELACIÓN: sintomas_diabetes -> sintomas_consulta (1:N)
    sintomas_consulta = relationship("sintomas_consulta", back_populates = "sintoma_diabetes")

# r4l.medicamentos_diabetes
class medicamentos_diabetes(Base):
    __tablename__ = "medicamentos_diabetes"
    __table_args__ = (
        Index("ix_medicamentos_diabetes_id_presentacion", "id_presentacion"), 
        Index("ix_medicamentos_diabetes_id_unidad", "id_unidad"), 
        {"schema": "r4l"}
    )

    id_medicamento_diabetes = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL MEDICAMENTO")
    id_presentacion = Column(Integer, ForeignKey("r4l.presentaciones_medicamentos.id_presentacion"), nullable = False, comment = "IDENTIFICADOR DE LA PRESENTACIÓN (FK)")
    id_unidad = Column(Integer, ForeignKey("r4l.unidades_medida.id_unidad"), nullable = False, comment = "IDENTIFICADOR DE LA UNIDAD DE MEDIDA (FK)")
    nombre = Column(String(50), nullable = False, comment = "NOMBRE DEL MEDICAMENTO")
    concentracion = Column(Integer, nullable = False, comment = "CONCENTRACIÓN DEL MEDICAMENTO")
    descripcion = Column(String(255), nullable = True, comment = "DESCRIPCIÓN DETALLADA")

    # RELACIÓN: medicamentos_diabetes -> presentaciones_medicamentos (N:1)
    presentacion = relationship("presentaciones_medicamentos", back_populates = "medicamentos_diabetes")
    # RELACIÓN: medicamentos_diabetes -> unidades_medida (N:1)
    unidad = relationship("unidades_medida", back_populates = "medicamentos_diabetes")
    # RELACIÓN: medicamentos_diabetes -> medicamentos_recetados (1:N)
    medicamentos_recetados = relationship("medicamentos_recetados", back_populates = "medicamento_diabetes")

# r4l.tipos_rutinas
class tipos_rutinas(Base):
    __tablename__ = "tipos_rutinas"
    __table_args__ = {"schema": "r4l"}

    id_tipo_rutina = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL TIPO DE RUTINA")
    nombre = Column(String(50), nullable = False, unique = True, comment = "NOMBRE DEL TIPO DE RUTINA")
    descripcion = Column(String(255), nullable = True, comment = "DESCRIPCIÓN DETALLADA")

    # RELACIÓN: tipos_rutinas -> rutinas_recetadas (1:N)
    rutinas_recetadas = relationship("rutinas_recetadas", back_populates = "tipo_rutina")

# r4l.estatus_citas
class estatus_citas(Base):
    __tablename__ = "estatus_citas"
    __table_args__ = {"schema": "r4l"}

    id_estatus_cita = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL ESTATUS DE LA CITA")
    nombre = Column(String(20), nullable = False, unique = True, comment = "NOMBRE DEL ESTATUS DE LA CITA")

    # RELACIÓN: estatus_citas -> citas_medicas (1:N)
    citas = relationship("citas_medicas", back_populates = "estatus")

# r4l.especialidades_medicas
class especialidades_medicas(Base):
    __tablename__ = "especialidades_medicas"
    __table_args__ = {"schema": "r4l"}

    id_especialidad = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA ESPECIALIDAD")
    nombre = Column(String(50), nullable = False, unique = True, comment = "NOMBRE DE LA ESPECIALIDAD")
    descripcion = Column(String(255), nullable = True, comment = "DESCRIPCIÓN DETALLADA")

    # RELACIÓN: especialidades_medicas -> medicos (1:N)
    medicos = relationship("medicos", back_populates = "especialidad")

# r4l.tipos_registros
class tipos_registros(Base):
    __tablename__ = "tipos_registros"
    __table_args__ = (
        Index("ix_tipos_registros_id_unidad", "id_unidad"), 
        {"schema": "r4l"}
    )

    id_tipo_registro = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL TIPO DE REGISTRO")
    id_unidad = Column(Integer, ForeignKey("r4l.unidades_medida.id_unidad"), nullable = False, comment = "IDENTIFICADOR DE LA UNIDAD DE MEDIDA (FK)")
    nombre = Column(String(50), nullable = False, unique = True, comment = "NOMBRE DEL TIPO DE REGISTRO")
    descripcion = Column(String(255), nullable = True, comment = "DESCRIPCIÓN DETALLADA")

    # RELACIÓN: tipos_registros -> unidades_medida (N:1)
    unidad = relationship("unidades_medida", back_populates = "tipos_registros")
    # RELACIÓN: tipos_registros -> registros_paciente (1:N)
    registros_paciente = relationship("registros_paciente", back_populates = "tipo_registro")


# ------------------------------------
# | MODELOS ORM - TABLAS PRINCIPALES |
# ------------------------------------

# r4l.datos_personales_medico
class datos_personales_medico(Base):
    __tablename__ = "datos_personales_medico"
    __table_args__ = (
        Index("ix_datos_personales_medico_id_sexo", "id_sexo"), 
        Index("ix_datos_personales_medico_id_pais", "id_pais"), 
        {"schema": "r4l"}
    )

    id_medico = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL MÉDICO")
    id_sexo = Column(Integer, ForeignKey("r4l.sexos.id_sexo"), nullable = False, comment = "IDENTIFICADOR DEL SEXO (FK)")
    id_pais = Column(Integer, ForeignKey("r4l.paises.id_pais"), nullable = False, comment = "IDENTIFICADOR DEL PAÍS (FK)")
    nombre_completo = Column(String(255), nullable = False, comment = "NOMBRE COMPLETO DEL MÉDICO")
    fecha_nacimiento = Column(Date, nullable = False, comment = "FECHA DE NACIMIENTO")
    telefono = Column(String(20), nullable = False, unique = True, comment = "TELÉFONO (ÚNICO)")
    fecha_hora_registro = Column(DateTime, nullable = False, comment = "FECHA Y HORA DE REGISTRO")
    fecha_hora_eliminacion = Column(DateTime, nullable = True, comment = "FECHA Y HORA DE ELIMINACIÓN (SI APLICA)")

    # RELACIÓN: datos_personales_medico -> sexos (N:1)
    sexo = relationship("sexos", back_populates = "datos_personales_medico")
    # RELACIÓN: datos_personales_medico -> paises (N:1)
    pais = relationship("paises", back_populates = "datos_personales_medico")
    # RELACIÓN: datos_personales_medico -> medicos (1:1)
    medico = relationship("medicos", back_populates = "datos_personales", uselist = False, cascade = "all, delete-orphan")

# r4l.medicos
class medicos(Base):
    __tablename__ = "medicos"
    __table_args__ = (
        Index("ix_medicos_id_rol", "id_rol"), 
        Index("ix_medicos_id_especialidad", "id_especialidad"), 
        Index("ix_medicos_id_estatus_usuario", "id_estatus_usuario"), 
        {"schema": "r4l"}
    )

    id_medico = Column(Integer, ForeignKey("r4l.datos_personales_medico.id_medico"), primary_key=True)
    id_rol = Column(Integer, ForeignKey("r4l.roles_usuarios.id_rol"), nullable=False)
    id_especialidad = Column(Integer, ForeignKey("r4l.especialidades_medicas.id_especialidad"), nullable=False)
    id_estatus_usuario = Column(Integer, ForeignKey("r4l.estatus_usuarios.id_estatus_usuario"), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True)
    cedula_profesional = Column(String(30), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    rfc = Column(String(13), nullable=False, unique=True)

    # RELACIÓN: medicos -> datos_personales_medico (1:1)
    datos_personales = relationship("datos_personales_medico", back_populates="medico")
    # RELACIÓN: medicos -> roles_usuarios (N:1)
    rol = relationship("roles_usuarios", back_populates="medicos")
    # RELACIÓN: medicos -> especialidades_medicas (N:1)
    especialidad = relationship("especialidades_medicas", back_populates="medicos")
    # RELACIÓN: medicos -> estatus_usuarios (N:1)
    estatus = relationship("estatus_usuarios", back_populates="medicos")
    # RELACIÓN: medicos -> horarios_medicos (1:N)
    horarios = relationship("horarios_medicos", back_populates="medico", cascade="all, delete-orphan")
    # RELACIÓN: medicos -> citas_medicas (1:N)
    citas = relationship("citas_medicas", back_populates="medico")
    # RELACIÓN: medicos -> consultas_medicas (1:N)
    consultas = relationship("consultas_medicas", back_populates="medico")
    # RELACIÓN: medicos -> usuarios (1:1, OPCIONAL)
    usuario = relationship("usuarios", back_populates="medico", uselist=False)
    # AGREGAR ESTA LÍNEA:
    pacientes = relationship("pacientes", back_populates="medico")

# r4l.horarios_medicos
class horarios_medicos(Base):
    __tablename__ = "horarios_medicos"
    __table_args__ = (
        Index("ix_horarios_medicos_id_medico", "id_medico"), 
        Index("ix_horarios_medicos_dia_semana", "dia_semana"), 
        {"schema": "r4l"}
    )

    id_horario = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL HORARIO")
    id_medico = Column(Integer, ForeignKey("r4l.medicos.id_medico"), nullable = False, comment = "IDENTIFICADOR DEL MÉDICO (FK)")
    dia_semana = Column(SmallInteger, nullable = False, comment = "DÍA DE LA SEMANA (1-7)")
    hora_inicio = Column(Time, nullable = False, comment = "HORA DE INICIO")
    hora_fin = Column(Time, nullable = False, comment = "HORA DE FIN")
    activo = Column(Boolean, nullable = False, comment = "INDICA SI EL HORARIO ESTÁ ACTIVO")

    # RELACIÓN: horarios_medicos -> medicos (N:1)
    medico = relationship("medicos", back_populates = "horarios")

# r4l.pacientes
class pacientes(Base):
    __tablename__ = "pacientes"
    
    __table_args__ = (
        Index("ix_pacientes_id_sexo", "id_sexo"), 
        Index("ix_pacientes_id_estatus_usuario", "id_estatus_usuario"), 
        Index("ix_pacientes_id_tipo_diabetes", "id_tipo_diabetes"), 
        {
            "schema": "r4l",
            "implicit_returning": False
        }
    )

    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    id_medico = Column(Integer, ForeignKey("r4l.medicos.id_medico"), nullable=True)  # Agregar esta línea
    id_sexo = Column(Integer, ForeignKey("r4l.sexos.id_sexo"), nullable=False)
    id_estatus_usuario = Column(Integer, ForeignKey("r4l.estatus_usuarios.id_estatus_usuario"), nullable=False)
    id_tipo_diabetes = Column(Integer, ForeignKey("r4l.tipos_diabetes.id_tipo_diabetes"), nullable=True)
    codigo = Column(String(20), nullable=False, unique=True)
    nombre_completo = Column(String(255), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    fecha_hora_registro = Column(DateTime, nullable=False)
    fecha_hora_eliminacion = Column(DateTime, nullable=True)

    # RELACIÓN: pacientes -> sexos (N:1)
    sexo = relationship("sexos", back_populates="pacientes")
    # RELACIÓN: pacientes -> estatus_usuarios (N:1)
    estatus = relationship("estatus_usuarios", back_populates="pacientes")
    # RELACIÓN: pacientes -> tipos_diabetes (N:1)
    tipo_diabetes = relationship("tipos_diabetes", back_populates="pacientes")
    # RELACIÓN: pacientes -> citas_medicas (1:N)
    citas = relationship("citas_medicas", back_populates="paciente")
    # RELACIÓN: pacientes -> consultas_medicas (1:N)
    consultas = relationship("consultas_medicas", back_populates="paciente")
    # RELACIÓN: pacientes -> pacientes_aplicacion (1:1)
    aplicacion = relationship("pacientes_aplicacion", back_populates="paciente", uselist=False, cascade="all, delete-orphan")
    # RELACIÓN: pacientes -> registros_paciente (1:N)
    registros = relationship("registros_paciente", back_populates="paciente", cascade="all, delete-orphan")
    # RELACIÓN: pacientes -> usuarios (1:1, OPCIONAL)
    usuario = relationship("usuarios", back_populates="paciente", uselist=False)
    # AGREGAR ESTA LÍNEA:
    medico = relationship("medicos", back_populates="pacientes") 

# r4l.citas_medicas
class citas_medicas(Base):
    __tablename__ = "citas_medicas"
    __table_args__ = (
            Index("ix_citas_medicas_id_medico", "id_medico"), 
            Index("ix_citas_medicas_id_paciente", "id_paciente"), 
            Index("ix_citas_medicas_fecha", "fecha"), 
            Index("ix_citas_medicas_id_estatus_cita", "id_estatus_cita"), 
            {
                "schema": "r4l",
                "implicit_returning": False 
            }
        )

    id_cita = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA CITA")
    id_rol = Column(Integer, ForeignKey("r4l.roles_usuarios.id_rol"), nullable = False, comment = "IDENTIFICADOR DEL ROL (FK, QUIÉN SOLICITA)")
    id_medico = Column(Integer, ForeignKey("r4l.medicos.id_medico"), nullable = False, comment = "IDENTIFICADOR DEL MÉDICO (FK)")
    id_paciente = Column(Integer, ForeignKey("r4l.pacientes.id_paciente"), nullable = False, comment = "IDENTIFICADOR DEL PACIENTE (FK)")
    id_estatus_cita = Column(Integer, ForeignKey("r4l.estatus_citas.id_estatus_cita"), nullable = False, comment = "IDENTIFICADOR DEL ESTATUS DE LA CITA (FK)")
    fecha = Column(Date, nullable = False, comment = "FECHA DE LA CITA")
    hora = Column(Time, nullable = False, comment = "HORA DE LA CITA")
    motivo = Column(String(255), nullable = True, comment = "MOTIVO DE LA CONSULTA")
    notas = Column(String(255), nullable = True, comment = "NOTAS ADICIONALES")
    fecha_hora_solicitud = Column(DateTime, nullable = False, comment = "FECHA Y HORA DE SOLICITUD")

    # RELACIÓN: citas_medicas -> roles_usuarios (N:1)
    rol = relationship("roles_usuarios", back_populates = "citas")
    # RELACIÓN: citas_medicas -> medicos (N:1)
    medico = relationship("medicos", back_populates = "citas")
    # RELACIÓN: citas_medicas -> pacientes (N:1)
    paciente = relationship("pacientes", back_populates = "citas")
    # RELACIÓN: citas_medicas -> estatus_citas (N:1)
    estatus = relationship("estatus_citas", back_populates = "citas")
    # RELACIÓN: citas_medicas -> consultas_medicas (1:1, OPCIONAL)
    consulta = relationship("consultas_medicas", back_populates = "cita", uselist = False)

# r4l.consultas_medicas
class consultas_medicas(Base):
    __tablename__ = "consultas_medicas"
    __table_args__ = (
        Index("ix_consultas_medicas_id_cita", "id_cita"), 
        Index("ix_consultas_medicas_id_paciente", "id_paciente"), 
        Index("ix_consultas_medicas_id_medico", "id_medico"), 
        Index("ix_consultas_medicas_fecha", "fecha"), 
        {"schema": "r4l"}
    )

    id_consulta = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA CONSULTA")
    id_cita = Column(Integer, ForeignKey("r4l.citas_medicas.id_cita"), nullable = False, comment = "IDENTIFICADOR DE LA CITA (FK)")
    id_medico = Column(Integer, ForeignKey("r4l.medicos.id_medico"), nullable = False, comment = "IDENTIFICADOR DEL MÉDICO (FK)")
    id_paciente = Column(Integer, ForeignKey("r4l.pacientes.id_paciente"), nullable = False, comment = "IDENTIFICADOR DEL PACIENTE (FK)")
    fecha = Column(Date, nullable = False, comment = "FECHA DE LA CONSULTA")
    hora = Column(Time, nullable = False, comment = "HORA DE LA CONSULTA")
    peso = Column(Numeric(5, 2), nullable = True, comment = "PESO EN KG")
    altura = Column(SmallInteger, nullable = True, comment = "ALTURA EN CM")
    presion_sistolica = Column(SmallInteger, nullable = True, comment = "PRESIÓN SISTÓLICA (mmHg)")
    presion_diastolica = Column(SmallInteger, nullable = True, comment = "PRESIÓN DIASTÓLICA (mmHg)")
    frecuencia_cardiaca = Column(SmallInteger, nullable = True, comment = "FRECUENCIA CARDÍACA (LPM)")
    glucosa_ayunas = Column(Numeric(5, 2), nullable = True, comment = "GLUCOSA EN AYUNAS (mg/dL)")
    glucosa_postprandial = Column(Numeric(5, 2), nullable = True, comment = "GLUCOSA POSTPRANDIAL (mg/dL)")
    hemoglobina_glicosilada = Column(Numeric(4, 2), nullable = True, comment = "HEMOGLOBINA GLICOSILADA (%)")
    colesterol_total = Column(Numeric(5, 2), nullable = True, comment = "COLESTEROL TOTAL (mg/dL)")
    trigliceridos = Column(Numeric(5, 2), nullable = True, comment = "TRIGLICÉRIDOS (mg/dL)")
    nivel_insulina = Column(Numeric(5, 2), nullable = True, comment = "NIVEL DE INSULINA (µU/mL)")
    notas = Column(String(255), nullable = True, comment = "NOTAS DE LA CONSULTA")
    plan_tratamiento = Column(Text, nullable = True, comment = "PLAN DE TRATAMIENTO DETALLADO")

    # RELACIÓN: consultas_medicas -> citas_medicas (1:1)
    cita = relationship("citas_medicas", back_populates = "consulta")
    # RELACIÓN: consultas_medicas -> medicos (N:1)
    medico = relationship("medicos", back_populates = "consultas")
    # RELACIÓN: consultas_medicas -> pacientes (N:1)
    paciente = relationship("pacientes", back_populates = "consultas")
    # RELACIÓN: consultas_medicas -> sintomas_consulta (1:N)
    sintomas = relationship("sintomas_consulta", back_populates = "consulta", cascade = "all, delete-orphan")
    # RELACIÓN: consultas_medicas -> recetas_medicas (1:N)
    recetas = relationship("recetas_medicas", back_populates = "consulta", cascade = "all, delete-orphan")

# r4l.sintomas_consulta
class sintomas_consulta(Base):
    __tablename__ = "sintomas_consulta"
    __table_args__ = (
        Index("ix_sintomas_consulta_id_consulta", "id_consulta"), 
        Index("ix_sintomas_consulta_id_sintoma_diabetes", "id_sintoma_diabetes"), 
        {"schema": "r4l"}
    )

    id_sintoma = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL SÍNTOMA EN CONSULTA")
    id_consulta = Column(Integer, ForeignKey("r4l.consultas_medicas.id_consulta"), nullable = False, comment = "IDENTIFICADOR DE LA CONSULTA (FK)")
    id_sintoma_diabetes = Column(Integer, ForeignKey("r4l.sintomas_diabetes.id_sintoma_diabetes"), nullable = False, comment = "IDENTIFICADOR DEL SÍNTOMA DE DIABETES (FK)")
    intensidad = Column(SmallInteger, nullable = True, comment = "INTENSIDAD (1-10)")
    duracion = Column(String(50), nullable = True, comment = "DURACIÓN DEL SÍNTOMA")
    notas = Column(String(255), nullable = True, comment = "NOTAS ADICIONALES")

    # RELACIÓN: sintomas_consulta -> consultas_medicas (N:1)
    consulta = relationship("consultas_medicas", back_populates = "sintomas")
    # RELACIÓN: sintomas_consulta -> sintomas_diabetes (N:1)
    sintoma_diabetes = relationship("sintomas_diabetes", back_populates = "sintomas_consulta")

# r4l.recetas_medicas
class recetas_medicas(Base):
    __tablename__ = "recetas_medicas"
    __table_args__ = (
        Index("ix_recetas_medicas_id_consulta", "id_consulta"), 
        {"schema": "r4l"}
    )

    id_receta = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA RECETA")
    id_consulta = Column(Integer, ForeignKey("r4l.consultas_medicas.id_consulta"), nullable = False, comment = "IDENTIFICADOR DE LA CONSULTA (FK)")
    fecha = Column(Date, nullable = False, comment = "FECHA DE EMISIÓN")
    hora = Column(Time, nullable = False, comment = "HORA DE EMISIÓN")
    instrucciones_generales = Column(String(255), nullable = True, comment = "INSTRUCCIONES GENERALES")
    url_pdf = Column(String(255), nullable = True, comment = "URL DEL PDF DE LA RECETA")

    # RELACIÓN: recetas_medicas -> consultas_medicas (N:1)
    consulta = relationship("consultas_medicas", back_populates = "recetas")
    # RELACIÓN: recetas_medicas -> medicamentos_recetados (1:N)
    medicamentos = relationship("medicamentos_recetados", back_populates = "receta", cascade = "all, delete-orphan")
    # RELACIÓN: recetas_medicas -> rutinas_recetadas (1:N)
    rutinas = relationship("rutinas_recetadas", back_populates = "receta", cascade = "all, delete-orphan")

# r4l.medicamentos_recetados
class medicamentos_recetados(Base):
    __tablename__ = "medicamentos_recetados"
    __table_args__ = (
        Index("ix_medicamentos_recetados_id_receta", "id_receta"), 
        {"schema": "r4l"}
    )

    id_medicamento = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL MEDICAMENTO RECETADO")
    id_receta = Column(Integer, ForeignKey("r4l.recetas_medicas.id_receta"), nullable = False, comment = "IDENTIFICADOR DE LA RECETA (FK)")
    id_medicamento_diabetes = Column(Integer, ForeignKey("r4l.medicamentos_diabetes.id_medicamento_diabetes"), nullable = False, comment = "IDENTIFICADOR DEL MEDICAMENTO DE DIABETES (FK)")
    dosis = Column(String(50), nullable = False, comment = "DOSIS PRESCRITA")
    frecuencia = Column(String(50), nullable = False, comment = "FRECUENCIA DE ADMINISTRACIÓN")
    duracion = Column(String(50), nullable = True, comment = "DURACIÓN DEL TRATAMIENTO")
    instrucciones_adicionales = Column(String(500), nullable = True, comment = "INSTRUCCIONES ADICIONALES")

    # RELACIÓN: medicamentos_recetados -> recetas_medicas (N:1)
    receta = relationship("recetas_medicas", back_populates = "medicamentos")
    # RELACIÓN: medicamentos_recetados -> medicamentos_diabetes (N:1)
    medicamento_diabetes = relationship("medicamentos_diabetes", back_populates = "medicamentos_recetados")

# r4l.rutinas_recetadas
class rutinas_recetadas(Base):
    __tablename__ = "rutinas_recetadas"
    __table_args__ = (
        Index("ix_rutinas_recetadas_id_receta", "id_receta"), 
        {"schema": "r4l"}
    )

    id_rutina = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DE LA RUTINA RECETADA")
    id_receta = Column(Integer, ForeignKey("r4l.recetas_medicas.id_receta"), nullable = False, comment = "IDENTIFICADOR DE LA RECETA (FK)")
    id_tipo_rutina = Column(Integer, ForeignKey("r4l.tipos_rutinas.id_tipo_rutina"), nullable = False, comment = "IDENTIFICADOR DEL TIPO DE RUTINA (FK)")
    id_comida = Column(Integer, ForeignKey("r4l.comidas.id_comida"), nullable = True, comment = "IDENTIFICADOR DE LA COMIDA (FK, SI APLICA)")
    descripcion = Column(String(500), nullable = False, comment = "DESCRIPCIÓN DE LA RUTINA")
    frecuencia = Column(String(50), nullable = True, comment = "FRECUENCIA")
    duracion = Column(String(50), nullable = True, comment = "DURACIÓN")
    notas = Column(String(255), nullable = True, comment = "NOTAS ADICIONALES")

    # RELACIÓN: rutinas_recetadas -> recetas_medicas (N:1)
    receta = relationship("recetas_medicas", back_populates = "rutinas")
    # RELACIÓN: rutinas_recetadas -> tipos_rutinas (N:1)
    tipo_rutina = relationship("tipos_rutinas", back_populates = "rutinas_recetadas")
    # RELACIÓN: rutinas_recetadas -> comidas (N:1, OPCIONAL)
    comida = relationship("comidas", back_populates = "rutinas_recetadas")

# r4l.pacientes_aplicacion
class pacientes_aplicacion(Base):
    __tablename__ = "pacientes_aplicacion"
    __table_args__ = (
        Index("ix_pacientes_aplicacion_id_sexo", "id_sexo"), 
        Index("ix_pacientes_aplicacion_id_pais", "id_pais"), 
        Index("ix_pacientes_aplicacion_id_estatus_usuario", "id_estatus_usuario"), 
        {"schema": "r4l"}
    )

    id_paciente = Column(Integer, ForeignKey("r4l.pacientes.id_paciente"), primary_key = True, comment = "IDENTIFICADOR ÚNICO DEL PACIENTE (FK)")
    id_sexo = Column(Integer, ForeignKey("r4l.sexos.id_sexo"), nullable = False, comment = "IDENTIFICADOR DEL SEXO (FK)")
    id_pais = Column(Integer, ForeignKey("r4l.paises.id_pais"), nullable = False, comment = "IDENTIFICADOR DEL PAÍS (FK)")
    id_estatus_usuario = Column(Integer, ForeignKey("r4l.estatus_usuarios.id_estatus_usuario"), nullable = False, comment = "IDENTIFICADOR DEL ESTATUS (FK)")
    nombre_completo = Column(String(255), nullable = False, comment = "NOMBRE COMPLETO DEL PACIENTE")
    fecha_nacimiento = Column(Date, nullable = False, comment = "FECHA DE NACIMIENTO")
    email = Column(String(255), nullable = False, unique = True, comment = "CORREO ELECTRÓNICO")
    telefono = Column(String(20), nullable = False, unique = True, comment = "TELÉFONO")
    fecha_registro = Column(Date, nullable = False, comment = "FECHA DE REGISTRO EN LA APLICACIÓN")
    fecha_hora_eliminacion = Column(DateTime, nullable = True, comment = "FECHA Y HORA DE ELIMINACIÓN (SI APLICA)")

    # RELACIÓN: pacientes_aplicacion -> pacientes (1:1)
    paciente = relationship("pacientes", back_populates = "aplicacion")
    # RELACIÓN: pacientes_aplicacion -> sexos (N:1)
    sexo = relationship("sexos", back_populates = "pacientes_aplicacion")
    # RELACIÓN: pacientes_aplicacion -> paises (N:1)
    pais = relationship("paises", back_populates = "pacientes_aplicacion")
    # RELACIÓN: pacientes_aplicacion -> estatus_usuarios (N:1)
    estatus = relationship("estatus_usuarios", back_populates = "pacientes_aplicacion")

# r4l.registros_paciente
class registros_paciente(Base):
    __tablename__ = "registros_paciente"
    __table_args__ = (
            Index("ix_registros_paciente_id_paciente", "id_paciente"), 
            Index("ix_registros_paciente_id_tipo_registro", "id_tipo_registro"), 
            Index("ix_registros_paciente_fecha", "fecha"), 
            {
                "schema": "r4l",
                "implicit_returning": False 
            }
        )

    id_registro = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL REGISTRO")
    id_paciente = Column(Integer, ForeignKey("r4l.pacientes.id_paciente"), nullable = False, comment = "IDENTIFICADOR DEL PACIENTE (FK)")
    id_tipo_registro = Column(Integer, ForeignKey("r4l.tipos_registros.id_tipo_registro"), nullable = False, comment = "IDENTIFICADOR DEL TIPO DE REGISTRO (FK)")
    fecha = Column(Date, nullable = False, comment = "FECHA DEL REGISTRO")
    hora = Column(Time, nullable = False, comment = "HORA DEL REGISTRO")
    valor = Column(Numeric(10, 2), nullable = False, comment = "VALOR REGISTRADO")
    unidad_alternativa = Column(String(20), nullable = True, comment = "UNIDAD DE MEDIDA ALTERNATIVA (SI CORRESPONDE)")
    notas = Column(String(255), nullable = True, comment = "NOTAS ADICIONALES")

    paciente = relationship("pacientes", back_populates = "registros")
    tipo_registro = relationship("tipos_registros", back_populates = "registros_paciente")

# r4l.usuarios
class usuarios(Base):
    __tablename__ = "usuarios"
    __table_args__ = (
        Index("ix_usuarios_id_medico", "id_medico"), 
        Index("ix_usuarios_id_paciente", "id_paciente"), 
        {
            "schema": "r4l",
            "implicit_returning": False
        }
    )

    id_usuario = Column(Integer, primary_key = True, autoincrement = True, comment = "IDENTIFICADOR ÚNICO DEL USUARIO")
    id_rol = Column(Integer, ForeignKey("r4l.roles_usuarios.id_rol"), nullable = False, comment = "IDENTIFICADOR DEL ROL (FK)")
    id_medico = Column(Integer, ForeignKey("r4l.medicos.id_medico"), nullable = True, unique = True, comment = "IDENTIFICADOR DEL MÉDICO (FK, ÚNICO SI APLICA)")
    id_paciente = Column(Integer, ForeignKey("r4l.pacientes.id_paciente"), nullable = True, unique = True, comment = "IDENTIFICADOR DEL PACIENTE (FK, ÚNICO SI APLICA)")
    contrasena = Column(String(255), nullable = False, comment = "CONTRASEÑA (HASH)")
    fecha_registro = Column(Date, nullable = False, comment = "FECHA DE REGISTRO")
    fecha_hora_eliminacion = Column(DateTime, nullable = True, comment = "FECHA Y HORA DE ELIMINACIÓN (SI APLICA)")

    # RELACIÓN: usuarios -> roles_usuarios (N:1)
    rol = relationship("roles_usuarios", back_populates = "usuarios")
    # RELACIÓN: usuarios -> medicos (1:1, OPCIONAL)
    medico = relationship("medicos", back_populates = "usuario")
    # RELACIÓN: usuarios -> pacientes (1:1, OPCIONAL)
    paciente = relationship("pacientes", back_populates = "usuario")