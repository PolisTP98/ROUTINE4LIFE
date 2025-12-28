# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# -------------------------------------
# | CREAR MODELO ORM DE "r4l.comidas" |
# -------------------------------------

class Comidas(Base):
    __tablename__ = "comidas"
    __table_args__ = {"schema": "r4l"}
    
    id_comida: Mapped[int] = mapped_column(
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
    
    # "rutina_alimentacion.py" TIENE LLAVE FORÁNEA CON "comidas.py"
    rutina_alimentacion: Mapped[list["RutinaAlimentacion"]] = relationship(
        "RutinaAlimentacion", 
        back_populates = "comidas"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<Comidas(id_comida = {self.id_comida}, nombre = '{self.nombre}')>"