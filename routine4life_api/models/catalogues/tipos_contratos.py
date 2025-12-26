# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# ---------------------------------------------
# | CREAR MODELO ORM DE "r4l.tipos_contratos" |
# ---------------------------------------------

class TiposContratos(Base):
    __tablename__ = 'tipos_contratos'
    __table_args__ = {'schema': 'r4l'}
    
    id_contrato: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(50), 
        nullable = False
    )
    
    def __repr__(self):
        return f"<TiposContratos(id_contrato = {self.id_contrato}, nombre = '{self.nombre}')>"