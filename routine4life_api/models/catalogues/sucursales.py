# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# ----------------------------------------
# | CREAR MODELO ORM DE "r4l.sucursales" |
# ----------------------------------------

class Sucursales(Base):
    __tablename__ = "sucursales"
    __table_args__ = {"schema": "r4l"}
    
    id_sucursal: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    ubicacion: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    codigo: Mapped[str] = mapped_column(
        String(10), 
        nullable = False, 
        unique = True
    )
    

    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "medico_laboral.py" TIENE LLAVE FORÁNEA CON "sucursales.py"
    medico_laboral: Mapped[list["MedicoLaboral"]] = relationship(
        "MedicoLaboral", 
        back_populates = "sucursales"
    )


    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<Sucursales(id_sucursal = {self.id_sucursal}, nombre = '{self.nombre}', codigo = '{self.codigo}')>"