# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# ---------------------------------------------------
# | CREAR MODELO ORM DE "r4l.especialidades_medico" |
# ---------------------------------------------------

class EspecialidadesMedico(Base):
    __tablename__ = "especialidades_medico"
    __table_args__ = {"schema": "r4l"}
    
    id_especialidad_medico: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        autoincrement = True
    )
    id_medico: Mapped[int] = mapped_column(
        Integer, 
        nullable = False
    )
    id_especialidad: Mapped[int] = mapped_column(
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
    institucion_graduacion: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    cedula_profesional: Mapped[str] = mapped_column(
        String(50), 
        nullable = False, 
        unique = True
    )
    
    
    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "medico_personal.py" TIENE LLAVE FORÁNEA CON "especialidades.py"
    medico_personal: Mapped["MedicoPersonal"] = relationship(
        "MedicoPersonal", 
        back_populates = "especialidades"
    )

    # "especialidades_medico.py" TIENE LLAVE FORÁNEA CON "especialidades.py"
    especialidades: Mapped["Especialidades"] = relationship(
        "Especialidades", 
        back_populates = "especialidades_medico"
    )

    # "especialidades_medico.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "especialidades_medico"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<EspecialidadesMedico(id_especialidad_medico = {self.id_especialidad_medico}, cedula = '{self.cedula_profesional}')>"