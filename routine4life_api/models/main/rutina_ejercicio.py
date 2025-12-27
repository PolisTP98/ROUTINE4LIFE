# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint
from database import Base


# ----------------------------------------------
# | CREAR MODELO ORM DE "r4l.rutina_ejercicio" |
# ----------------------------------------------

class RutinaEjercicio(Base):
    __tablename__ = "rutina_ejercicio"
    __table_args__ = (
        {"schema": "r4l"}, 
        CheckConstraint("fecha_fin IS NULL OR fecha_fin >= fecha_inicio", name = "chk_fechas_rutina_ejercicio"), 
        CheckConstraint("duracion_minutos > 0", name = "chk_duracion_rutina_ejercicio"), 
        CheckConstraint("frecuencia_semanal > 0", name = "chk_frecuencia_rutina_ejercicio")
    )
    
    id_rutina_ejercicio: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    id_cita: Mapped[int] = mapped_column(
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
    ejercicio: Mapped[str] = mapped_column(
        String(100), 
        nullable = False
    )
    duracion_minutos: Mapped[int] = mapped_column(
        SmallInteger, 
        nullable = False
    )
    intensidad: Mapped[str] = mapped_column(
        String(50), 
        nullable = False
    )
    frecuencia_semanal: Mapped[int] = mapped_column(
        SmallInteger, 
        nullable = False
    )
    observaciones: Mapped[str | None] = mapped_column(
        String(255), 
        nullable = True
    )
    

    # -----------------
    # | RELATIONSHIPS |
    # -----------------
    
    # "rutina_ejercicio.py" TIENE LLAVE FORÁNEA CON "cita_paciente.py"
    cita_paciente: Mapped["CitaPaciente"] = relationship(
        "CitaPaciente", 
        back_populates = "rutina_ejercicio"
    )

    # "rutina_ejercicio.py" TIENE LLAVE FORÁNEA CON "estatus_paciente.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "rutina_ejercicio"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<RutinaEjercicio(id_rutina_ejercicio = {self.id_rutina_ejercicio}, ejercicio = '{self.ejercicio}', duracion = {self.duracion_minutos} min)>"