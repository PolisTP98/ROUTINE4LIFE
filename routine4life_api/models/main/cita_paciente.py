# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date, time
from decimal import Decimal
from sqlalchemy import Integer, String, Date, Time, DECIMAL, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint
from database import Base


# -------------------------------------------
# | CREAR MODELO ORM DE "r4l.cita_paciente" |
# -------------------------------------------

class CitaPaciente(Base):
    __tablename__ = "cita_paciente"
    __table_args__ = (
        {"schema": "r4l"}, 
        CheckConstraint("peso > 0", name = "chk_peso"), 
        CheckConstraint("altura > 0", name = "chk_altura"), 
        CheckConstraint("frecuencia_cardiaca > 0", name = "chk_frecuencia_cardiaca"), 
        CheckConstraint("glucosa_ayuno >= 0", name = "chk_glucosa_ayuno"), 
        CheckConstraint("glucosa_postprandial >= 0", name = "chk_glucosa_postprandial"), 
        CheckConstraint("hba1c >= 0", name = "chk_hba1c"), 
        CheckConstraint("colesterol_total >= 0", name = "chk_colesterol"), 
        CheckConstraint("trigliceridos >= 0", name = "chk_trigliceridos"), 
        CheckConstraint("insulina_actual >= 0", name = "chk_insulina"), 
        CheckConstraint("fecha_siguiente_cita IS NULL OR fecha_siguiente_cita >= fecha_cita", 
                        name = "chk_fechas_cita")
    )
    
    id_cita: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    id_medico: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_paciente: Mapped[int] = mapped_column(
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
    fecha_cita: Mapped[date] = mapped_column(
        Date, 
        nullable = False, 
        server_default = "GETDATE()"
    )
    hora_cita: Mapped[time] = mapped_column(
        Time, 
        nullable = False
    )
    peso: Mapped[Decimal] = mapped_column(
        DECIMAL(5, 2), 
        nullable = False
    )
    altura: Mapped[int] = mapped_column(
        SmallInteger, 
        nullable = False
    )
    presion_arterial: Mapped[str] = mapped_column(
        String(10), 
        nullable = False
    )
    frecuencia_cardiaca: Mapped[int] = mapped_column(
        SmallInteger, 
        nullable = False
    )
    glucosa_ayuno: Mapped[Decimal] = mapped_column(
        DECIMAL(5, 2), 
        nullable = False
    )
    glucosa_postprandial: Mapped[Decimal] = mapped_column(
        DECIMAL(5, 2), 
        nullable = False
    )
    hba1c: Mapped[Decimal] = mapped_column(
        DECIMAL(4, 2), 
        nullable = False
    )
    colesterol_total: Mapped[Decimal] = mapped_column(
        DECIMAL(5, 2), 
        nullable = False
    )
    trigliceridos: Mapped[Decimal] = mapped_column(
        DECIMAL(5, 2), 
        nullable = False
    )
    insulina_actual: Mapped[Decimal] = mapped_column(
        DECIMAL(5, 2), 
        nullable = False
    )
    recomendaciones: Mapped[str | None] = mapped_column(
        String, 
        nullable = True
    )
    fecha_siguiente_cita: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    hora_siguiente_cita: Mapped[time | None] = mapped_column(
        Time, 
        nullable = True
    )
    
    
    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    medico_personal: Mapped["MedicoPersonal"] = relationship(
        "MedicoPersonal", 
        back_populates = "cita_paciente"
    )
    pacientes: Mapped["Pacientes"] = relationship(
        "Pacientes", 
        back_populates = "cita_paciente"
    )
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "cita_paciente"
    )
    rutina_ejercicio: Mapped[list["RutinaEjercicio"]] = relationship(
        "RutinaEjercicio", 
        back_populates = "cita_paciente", 
        cascade = "all, delete-orphan"
    )
    rutina_alimentacion: Mapped[list["RutinaAlimentacion"]] = relationship(
        "RutinaAlimentacion", 
        back_populates = "cita_paciente", 
        cascade = "all, delete-orphan"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<CitaPaciente(id_cita = {self.id_cita}, paciente_id = {self.id_paciente}, fecha = '{self.fecha_cita}')>"