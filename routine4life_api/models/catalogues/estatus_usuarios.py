# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# ----------------------------------------------
# | CREAR MODELO ORM DE "r4l.estatus_usuarios" |
# ----------------------------------------------

class EstatusUsuarios(Base):
    __tablename__ = "estatus_usuarios"
    __table_args__ = {"schema": "r4l"}
    
    id_estatus: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(50), 
        nullable = False
    )
    descripcion: Mapped[str | None] = mapped_column(
        String(100), 
        nullable = True
    )


    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    medico_personal: Mapped[list["MedicoPersonal"]] = relationship(
        "MedicoPersonal", 
        back_populates = "estatus_usuarios"
    )

    # "medico_laboral.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    medico_laboral: Mapped[list["MedicoLaboral"]] = relationship(
        "MedicoLaboral", 
        back_populates = "estatus_usuarios"
    )

    # "especialidades_medico.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    especialidades_medico: Mapped[list["EspecialidadesMedico"]] = relationship(
        "EspecialidadesMedico", 
        back_populates = "estatus_usuarios"
    )

    # "pacientes.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    pacientes: Mapped[list["Pacientes"]] = relationship(
        "Pacientes", 
        back_populates = "estatus_usuarios"
    )

    # "cita_paciente.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    cita_paciente: Mapped[list["CitaPaciente"]] = relationship(
        "CitaPaciente", 
        back_populates = "estatus_usuarios"
    )

    # "rutina_ejercicio.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    rutina_ejercicio: Mapped[list["RutinaEjercicio"]] = relationship(
        "RutinaEjercicio", 
        back_populates = "estatus_usuarios"
    )

    # "rutina_alimentacion.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    rutina_alimentacion: Mapped[list["RutinaAlimentacion"]] = relationship(
        "RutinaAlimentacion", 
        back_populates = "estatus_usuarios"
    )

    # "descripcion_rutina.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    descripcion_rutina: Mapped[list["DescripcionRutina"]] = relationship(
        "DescripcionRutina", 
        back_populates = "estatus_usuarios"
    )

    # "pacientes_aplicacion.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    pacientes_aplicacion: Mapped[list["PacientesAplicacion"]] = relationship(
        "PacientesAplicacion", 
        back_populates = "estatus_usuarios"
    )

    # "usuarios_pacientes.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    usuarios_pacientes: Mapped[list["UsuariosPacientes"]] = relationship(
        "UsuariosPacientes", 
        back_populates = "estatus_usuarios"
    )


    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------
    
    def __repr__(self):
        return f"<EstatusUsuarios(id_estatus = {self.id_estatus}, nombre = '{self.nombre}')>"