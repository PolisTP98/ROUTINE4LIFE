# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# ------------------------------------------------
# | CREAR MODELO ORM DE "r4l.descripcion_rutina" |
# ------------------------------------------------

class DescripcionRutina(Base):
    __tablename__ = "descripcion_rutina"
    __table_args__ = {"schema": "r4l"}
    
    id_rutina_alimentacion: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        nullable = False
    )
    id_estatus: Mapped[int] = mapped_column(
        Integer, 
        nullable = False, 
        default = 1
    )
    fecha_eliminacion: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    fecha_reactivacion: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    fecha_registro: Mapped[date] = mapped_column(
        Date, 
        nullable = False, 
        server_default = "GETDATE()"
    )
    descripcion: Mapped[str] = mapped_column(
        String, 
        nullable = False
    )
    
    
    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "descripcion_rutina.py" TIENE LLAVE PRIMARIA CON "rutina_alimentacion.py"
    rutina_alimentacion: Mapped["RutinaAlimentacion"] = relationship(
        "RutinaAlimentacion", 
        back_populates = "descripcion_rutina", 
        foreign_keys = [id_rutina_alimentacion]
    )

    # "descripcion_rutina.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "descripcion_rutina"
    )


    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------
    
    def __repr__(self):
        descripcion_corta = self.descripcion[:50] + "..." if len(self.descripcion) > 50 else self.descripcion
        return f"<DescripcionRutina(id_rutina_alimentacion = {self.id_rutina_alimentacion}, descripcion = '{descripcion_corta}')>"