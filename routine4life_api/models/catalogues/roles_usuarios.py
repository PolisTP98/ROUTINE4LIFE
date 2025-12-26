# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# --------------------------------------------
# | CREAR MODELO ORM DE "r4l.roles_usuarios" |
# --------------------------------------------

class RolesUsuarios(Base):
    __tablename__ = 'roles_usuarios'
    __table_args__ = {'schema': 'r4l'}
    
    id_rol: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(50), 
        nullable = False
    )
    
    def __repr__(self):
        return f"<RolesUsuarios(id_rol = {self.id_rol}, nombre = '{self.nombre}')>"