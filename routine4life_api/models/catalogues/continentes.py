# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# -----------------------------------------
# | CREAR MODELO ORM DE "r4l.continentes" |
# -----------------------------------------

class Continentes(Base):
    __tablename__ = 'continentes'
    __table_args__ = {'schema': 'r4l'}
    
    id_continente: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(20), 
        nullable = False
    )
    
    # ESTABLECER "relationship" CON "Paises"
    # "paises.py" TIENE LLAVE FORÁNEA CON "continentes.py"
    paises: Mapped[list["Paises"]] = relationship(
        back_populates = "continente",
        cascade = "all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Continentes(id_continente = {self.id_continente}, nombre = '{self.nombre}')>"