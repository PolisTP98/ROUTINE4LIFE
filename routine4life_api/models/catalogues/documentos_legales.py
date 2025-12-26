# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# -----------------------------------------------
# | CREAR MODELO ORM DE "r4l.documentoslegales" |
# -----------------------------------------------

class DocumentosLegales(Base):
    __tablename__ = 'documentos_legales'
    __table_args__ = {'schema': 'r4l'}
    
    id_documento: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    
    def __repr__(self):
        return f"<DocumentosLegales(id_documento = {self.id_documento}, nombre = '{self.nombre}')>"