# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# -----------------------------------------------
# | CREAR MODELO ORM DE "r4l.documentoslegales" |
# -----------------------------------------------

class DocumentosLegales(Base):
    __tablename__ = "documentos_legales"
    __table_args__ = {"schema": "r4l"}
    
    id_documento: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    nombre: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )


    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "documentos_legales.py"
    medico_personal: Mapped[list["MedicoPersonal"]] = relationship(
        "MedicoPersonal", 
        back_populates = "documentos_legales"
    )


    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------
    
    def __repr__(self):
        return f"<DocumentosLegales(id_documento = {self.id_documento}, nombre = '{self.nombre}')>"