# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# -------------------------------------------
# | CREAR MODELO ORM DE "r4l.departamentos" |
# -------------------------------------------

class Departamentos(Base):
    __tablename__ = "departamentos"
    __table_args__ = {"schema": "r4l"}
    
    id_departamento: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )


    # -----------------
    # | RELATIONSHIPS |
    # -----------------
    
    # "medico_laboral.py" TIENE LLAVE FORÁNEA CON "departamentos.py"
    medico_laboral: Mapped[list["MedicoLaboral"]] = relationship(
        "MedicoLaboral", 
        back_populates = "departamentos"
    )


    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<Departamentos(id_departamento = {self.id_departamento}, nombre = '{self.nombre}')>"