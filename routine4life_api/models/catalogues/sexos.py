# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# -----------------------------------
# | CREAR MODELO ORM DE "r4l.sexos" |
# -----------------------------------

class Sexos(Base):
    __tablename__ = 'sexos'
    __table_args__ = {'schema': 'r4l'}
    
    id_sexo: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(20), 
        nullable = False
    )
    
    def __repr__(self):
        return f"<Sexos(id_sexo = {self.id_sexo}, nombre = '{self.nombre}')>"