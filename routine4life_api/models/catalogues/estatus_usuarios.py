# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# ----------------------------------------------
# | CREAR MODELO ORM DE "r4l.estatus_usuarios" |
# ----------------------------------------------

class EstatusUsuarios(Base):
    __tablename__ = 'estatus_usuarios'
    __table_args__ = {'schema': 'r4l'}
    
    id_estatus: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(50), 
        nullable = False
    )
    descripcion: Mapped[str | None] = mapped_column(
        String(100), 
        nullable = True
    )
    
    def __repr__(self):
        return f"<EstatusUsuarios(id_estatus = {self.id_estatus}, nombre = '{self.nombre}')>"