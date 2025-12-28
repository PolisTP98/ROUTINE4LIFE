# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint
from database import Base


# ------------------------------------------------
# | CREAR MODELO ORM DE "r4l.usuarios_pacientes" |
# ------------------------------------------------

class UsuariosPacientes(Base):
    __tablename__ = "usuarios_pacientes"
    __table_args__ = (
        {"schema": "r4l"}, 
        CheckConstraint("fecha_eliminacion IS NULL OR fecha_eliminacion >= fecha_registro", name = "chk_fechas")
    )
    
    id_paciente_aplicacion: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True, 
        nullable = False
    )
    id_rol: Mapped[int] = mapped_column(
        Integer, 
        nullable = False, 
        default = 3
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
    username: Mapped[str] = mapped_column(
        String(50), 
        nullable = False
    )
    email: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    contrasena_cifrada: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    url_imagen_perfil: Mapped[str] = mapped_column(
        String(255), 
        nullable = False
    )
    

    # -----------------
    # | RELATIONSHIPS |
    # -----------------

    # "usuarios_pacientes.py" TIENE LLAVE PRIMARIA CON "pacientes_aplicacion.py"
    pacientes_aplicacion: Mapped["PacientesAplicacion"] = relationship(
        "PacientesAplicacion", 
        back_populates = "usuarios_pacientes", 
        foreign_keys = [id_paciente_aplicacion]
    )

    # "usuarios_pacientes.py" TIENE LLAVE FORÁNEA CON "roles_usuarios.py"
    roles_usuarios: Mapped["RolesUsuarios"] = relationship(
        "RolesUsuarios", 
        back_populates = "usuarios_pacientes"
    )

    # "usuarios_pacientes.py" TIENE LLAVE FORÁNEA CON "estatus_usuarios.py"
    estatus_usuarios: Mapped["EstatusUsuarios"] = relationship(
        "EstatusUsuarios", 
        back_populates = "usuarios_pacientes"
    )
    

    # ----------------------------------------
    # | MOSTRAR OBJETO DE MANERA INFORMATIVA |
    # ----------------------------------------

    def __repr__(self):
        return f"<UsuariosPacientes(id_paciente_aplicacion = {self.id_paciente_aplicacion}, username = '{self.username}', email = '{self.email}')>"