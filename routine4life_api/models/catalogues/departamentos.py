# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# -------------------------------------------
# | CREAR MODELO ORM DE "r4l.departamentos" |
# -------------------------------------------

class Departamentos(Base):
    __tablename__ = 'departamentos'
    __table_args__ = {'schema': 'r4l'}
    
    id_departamento: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    
    def __repr__(self):
        return f"<Departamentos(id_departamento = {self.id_departamento}, nombre = '{self.nombre}')>"