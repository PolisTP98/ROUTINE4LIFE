# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# ---------------------------------------------
# | CREAR MODELO ORM DE "r4l.medico_personal" |
# ---------------------------------------------

class MedicoPersonal(Base):
    __tablename__ = "medico_personal"
    __table_args__ = {"schema": "r4l"}
    
    id_medico: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    id_sexo: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_pais: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_documento: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_estatus: Mapped[int] = mapped_column(
        Integer, 
        nullable = False, 
        default = 1
    )
    fecha_eliminacion: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    fecha_suspension: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    fecha_reactivacion: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    fecha_registro: Mapped[date] = mapped_column(
        Date, 
        nullable = False, 
        server_default = "GETDATE()"
    )
    numero_identificacion: Mapped[str] = mapped_column(
        VARCHAR(50), 
        nullable = False, 
        unique = True
    )
    nombres: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    apellido_paterno: Mapped[str] = mapped_column(
        String(50), 
        nullable = False
    )
    apellido_materno: Mapped[str | None] = mapped_column(
        String(50), 
        nullable = True
    )
    fecha_nacimiento: Mapped[date] = mapped_column(
        Date, 
        nullable = False
    )
    telefono: Mapped[str] = mapped_column(
        VARCHAR(20), 
        nullable = False, 
        unique = True
    )
    email_personal: Mapped[str] = mapped_column(
        String(255), 
        nullable = False, 
        unique = True
    )
    rfc: Mapped[str] = mapped_column(
        VARCHAR(13), 
        nullable = False, 
        unique = True
    )
    direccion: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    

    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "sexos.py"
    sexos: Mapped["Sexos"] = relationship(
        "Sexos", 
        back_populates = "medico_personal"
    )

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "paises.py"
    paises: Mapped["Paises"] = relationship(
        "Paises", 
        back_populates = "medico_personal"
    )

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "documentos_legales.py"
    documentos_legales: Mapped["DocumentosLegales"] = relationship(
        "DocumentosLegales", 
        back_populates = "medico_personal"
    )

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "medico_personal"
    )

    # "medico_laboral.py" TIENE LLAVE PRIMARIA CON "medico_personal.py"
    medico_laboral: Mapped["MedicoLaboral"] = relationship(
        "MedicoLaboral", 
        back_populates = "medico_personal", 
        cascade = "all, delete-orphan", 
        uselist = False
    )

    # "especialidades_medico.py" TIENE LLAVE FORÁNEA CON "medico_personal.py"
    especialidades_medico: Mapped[list["EspecialidadesMedico"]] = relationship(
        "EspecialidadesMedico", 
        back_populates = "medico_personal", 
        cascade = "all, delete-orphan"
    )

    # "cita_paciente.py" TIENE LLAVE FORÁNEA CON "medico_personal.py"
    cita_paciente: Mapped[list["CitaPaciente"]] = relationship(
        "CitaPaciente", 
        back_populates = "medico_personal"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<MedicoPersonal(id_medico = {self.id_medico}, nombres = '{self.nombres} {self.apellido_paterno}')>"