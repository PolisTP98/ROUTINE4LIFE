# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# ---------------------------------------
# | CREAR MODELO ORM DE "r4l.pacientes" |
# ---------------------------------------

class Pacientes(Base):
    __tablename__ = "pacientes"
    __table_args__ = {"schema": "r4l"}
    
    id_paciente: Mapped[int] = mapped_column(
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
    id_estatus: Mapped[int] = mapped_column(
        Integer, 
        nullable = False, 
        default = 1
    )
    fecha_eliminacion: Mapped[date | None] = mapped_column(
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
    codigo: Mapped[str] = mapped_column(
        String(10), 
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
    
    
    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "pacientes.py" TIENE LLAVE FORÁNEA CON "sexos.py"
    sexos: Mapped["Sexos"] = relationship(
        "Sexos", 
        back_populates = "pacientes"
    )

    # "pacientes.py" TIENE LLAVE FORÁNEA CON "paises.py"
    paises: Mapped["Paises"] = relationship(
        "Paises", 
        back_populates = "pacientes"
    )

    # "pacientes.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "pacientes"
    )

    # "cita_paciente.py" TIENE LLAVE FORÁNEA CON "pacientes.py"
    cita_paciente: Mapped[list["CitaPaciente"]] = relationship(
        "CitaPaciente", 
        back_populates = "pacientes", 
        cascade = "all, delete-orphan"
    )

    # "pacientes_aplicacion.py" TIENE LLAVE PRIMARIA CON "pacientes.py"
    pacientes_aplicacion: Mapped[list["PacientesAplicacion"]] = relationship(
        "PacientesAplicacion", 
        back_populates = "pacientes", 
        cascade = "all, delete-orphan"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<Pacientes(id_paciente = {self.id_paciente}, codigo = '{self.codigo}', nombres = '{self.nombres}')>"