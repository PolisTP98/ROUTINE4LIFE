# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# --------------------------------------------
# | CREAR MODELO ORM DE "r4l.especialidades" |
# --------------------------------------------

class Especialidades(Base):
    __tablename__ = 'especialidades'
    __table_args__ = {'schema': 'r4l'}
    
    id_especialidad: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    
    def __repr__(self):
        return f"<Especialidades(id_especialidad = {self.id_especialidad}, nombre = '{self.nombre}')>"