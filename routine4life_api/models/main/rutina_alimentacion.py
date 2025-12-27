# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint
from database import Base


# -------------------------------------------------
# | CREAR MODELO ORM DE "r4l.rutina_alimentacion" |
# -------------------------------------------------

class RutinaAlimentacion(Base):
    __tablename__ = "rutina_alimentacion"
    __table_args__ = (
        {"schema": "r4l"}, 
        CheckConstraint("calorias_aprox >= 0", name = "chk_calorias"), 
        CheckConstraint("fecha_fin IS NULL OR fecha_fin >= fecha_inicio", name = "chk_fechas_rutina_alimentacion"), 
        CheckConstraint("duracion_dias > 0", name = "chk_duracion_dias")
    )
    
    id_rutina_alimentacion: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    id_cita: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_comida: Mapped[int] = mapped_column(
        Integer, 
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
    fecha_inicio: Mapped[date] = mapped_column(
        Date, 
        nullable = False, 
        server_default = "GETDATE()"
    )
    fecha_fin: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    platillo: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    calorias_aprox: Mapped[int] = mapped_column(
        SmallInteger, 
        nullable = False
    )
    duracion_dias: Mapped[int] = mapped_column(
        SmallInteger, 
        nullable = False
    )
    observaciones: Mapped[str | None] = mapped_column(
        String(255), 
        nullable = True
    )
    url_imagen_platillo: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    
    
    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "rutina_alimentacion.py" TIENE LLAVE FORÁNEA CON "cita_paciente.py"
    cita_paciente: Mapped["CitaPaciente"] = relationship(
        "CitaPaciente", 
        back_populates = "rutina_alimentacion"
    )

    # "rutina_alimentacion.py" TIENE LLAVE FORÁNEA CON "comidas.py"
    comidas: Mapped["Comidas"] = relationship(
        "Comidas", 
        back_populates = "rutina_alimentacion"
    )

    # "rutina_alimentacion.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "rutina_alimentacion"
    )

    # "rutina_alimentacion.py" TIENE LLAVE FORÁNEA CON "descripcion_rutina.py"
    descripcion_rutina: Mapped["DescripcionRutina"] = relationship(
        "DescripcionRutina", 
        back_populates = "rutina_alimentacion", 
        cascade = "all, delete-orphan", 
        uselist = False
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<RutinaAlimentacion(id_rutina_alimentacion = {self.id_rutina_alimentacion}, platillo = '{self.platillo}', calorias = {self.calorias_aprox})>"