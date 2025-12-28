# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# --------------------------------------------------
# | CREAR MODELO ORM DE "r4l.pacientes_aplicacion" |
# --------------------------------------------------

class PacientesAplicacion(Base):
    __tablename__ = "pacientes_aplicacion"
    __table_args__ = {"schema": "r4l"}
    
    id_paciente_aplicacion: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    id_paciente: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
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
    email: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    
    
    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "pacientes_aplicacion.py" TIENE LLAVE FORÁNEA CON "pacientes.py"
    pacientes: Mapped["Pacientes"] = relationship(
        "Pacientes", 
        back_populates = "pacientes_aplicacion"
    )

    # "pacientes_aplicacion.py" TIENE LLAVE FORÁNEA CON "sexos.py"
    sexos: Mapped["Sexos"] = relationship(
        "Sexos", 
        back_populates = "pacientes_aplicacion"
    )

    # "pacientes_aplicacion.py" TIENE LLAVE FORÁNEA CON "paises.py"
    paises: Mapped["Paises"] = relationship(
        "Paises", 
        back_populates = "pacientes_aplicacion"
    )

    # "pacientes_aplicacion.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "pacientes_aplicacion"
    )

    # "usuarios_pacientes.py" TIENE LLAVE PRIMARIA CON "pacientes_aplicacion.py"
    usuarios_pacientes: Mapped["UsuariosPacientes"] = relationship(
        "UsuariosPacientes", 
        back_populates = "pacientes_aplicacion", 
        cascade = "all, delete-orphan", 
        uselist = False
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<PacientesAplicacion(id_paciente_aplicacion = {self.id_paciente_aplicacion}, email = '{self.email}')>"