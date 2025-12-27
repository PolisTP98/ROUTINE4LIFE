# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint
from database import Base


# --------------------------------------------
# | CREAR MODELO ORM DE "r4l.medico_laboral" |
# --------------------------------------------

class MedicoLaboral(Base):
    __tablename__ = "medico_laboral"
    __table_args__ = (
        {"schema": "r4l"}, 
        CheckConstraint("anios_experiencia >= 0", name = "chk_anios_experiencia"), 
        CheckConstraint("fecha_fin IS NULL OR fecha_fin >= fecha_inicio", name = "chk_fechas_medico_laboral")
    )
    
    id_medico: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        nullable = False
    )
    id_sucursal: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_departamento: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_contrato: Mapped[int] = mapped_column(
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
    fecha_suspension: Mapped[date | None] = mapped_column(
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
        nullable = False
    )
    fecha_fin: Mapped[date | None] = mapped_column(
        Date, 
        nullable = True
    )
    anios_experiencia: Mapped[int] = mapped_column(
        SmallInteger, 
        nullable = False
    )
    nss: Mapped[str] = mapped_column(
        String(50), 
        nullable = False, 
        unique = True
    )


    # -----------------
    # | RELATIONSHIPS |
    # -----------------
    
    # "medico_laboral.py" TIENE LLAVE PRIMARIA CON "medico_personal.py"
    medico_personal: Mapped["MedicoPersonal"] = relationship(
        "MedicoPersonal", 
        back_populates = "medico_laboral", 
        foreign_keys = [id_medico]
    )

    # "medico_laboral.py" TIENE LLAVE FORÁNEA CON "sucursales.py"
    sucursales: Mapped["Sucursales"] = relationship(
        "Sucursales", 
        back_populates = "medico_laboral"
    )

    # "medico_laboral.py" TIENE LLAVE FORÁNEA CON "departamentos.py"
    departamentos: Mapped["Departamentos"] = relationship(
        "Departamentos", 
        back_populates = "medico_laboral"
    )

    # "medico_laboral.py" TIENE LLAVE FORÁNEA CON "tipos_contratos.py"
    tipos_contratos: Mapped["TiposContratos"] = relationship(
        "TiposContratos", 
        back_populates = "medico_laboral"
    )

    # "medico_laboral.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "medico_laboral"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<MedicoLaboral(id_medico = {self.id_medico}, nss = '{self.nss}')>"