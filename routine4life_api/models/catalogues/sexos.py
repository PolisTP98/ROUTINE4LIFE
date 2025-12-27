# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# -----------------------------------
# | CREAR MODELO ORM DE "r4l.sexos" |
# -----------------------------------

class Sexos(Base):
    __tablename__ = "sexos"
    __table_args__ = {"schema": "r4l"}
    
    id_sexo: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(20), 
        nullable = False
    )


    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "sexos.py"
    medico_personal: Mapped[list["MedicoPersonal"]] = relationship(
        "MedicoPersonal", 
        back_populates = "sexos"
    )

    # "pacientes.py" TIENE LLAVE FORÁNEA CON "sexos.py"
    pacientes: Mapped[list["Pacientes"]] = relationship(
        "Pacientes", 
        back_populates = "sexos"
    )

    # "pacientes_aplicacion.py" TIENE LLAVE FORÁNEA CON "sexos.py"
    pacientes_aplicacion: Mapped[list["PacientesAplicacion"]] = relationship(
        "PacientesAplicacion", 
        back_populates = "sexos"
    )


    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<Sexos(id_sexo = {self.id_sexo}, nombre = '{self.nombre}')>"