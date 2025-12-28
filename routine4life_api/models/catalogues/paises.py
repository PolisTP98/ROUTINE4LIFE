# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# ------------------------------------
# | CREAR MODELO ORM DE "r4l.paises" |
# ------------------------------------

class Paises(Base):
    __tablename__ = "paises"
    __table_args__ = {"schema": "r4l"}
    
    id_pais: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    id_continente: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("r4l.continentes.id_continente", ondelete = "CASCADE", onupdate = "CASCADE"), 
        nullable = False
    )
    nombre: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    codigo_iso: Mapped[str] = mapped_column(
        CHAR(5), 
        nullable = False
    )
    prefijo_telefonico: Mapped[str] = mapped_column(
        CHAR(5), 
        nullable = False
    )
    

    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "paises.py" TIENE LLAVE FORÁNEA CON "continentes.py"
    continentes: Mapped["Continentes"] = relationship(
        "Continentes", 
        back_populates = "paises"
    )

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "paises.py"
    medico_personal: Mapped[list["MedicoPersonal"]] = relationship(
        "MedicoPersonal", 
        back_populates = "paises"
    )

    # "pacientes.py" TIENE LLAVE FORÁNEA CON "paises.py"
    pacientes: Mapped[list["Pacientes"]] = relationship(
        "Pacientes", 
        back_populates = "paises"
    )

    # "pacientes_aplicacion.py" TIENE LLAVE FORÁNEA CON "paises.py"
    pacientes_aplicacion: Mapped[list["PacientesAplicacion"]] = relationship(
        "PacientesAplicacion", 
        back_populates = "paises"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<Paises(id_pais = {self.id_pais}, nombre = '{self.nombre}', codigo_iso = '{self.codigo_iso}')>"