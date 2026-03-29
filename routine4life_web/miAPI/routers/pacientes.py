# miAPI/routers/pacientes.py
import sys
import os

# Agregar la carpeta ROUTINE4LIFE al path
project_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from datetime import datetime, date

from miAPI.data.database import get_db
from miAPI.models.medicosPacientes import PacienteCreate, PacienteUpdate, PacienteResponse
from miAPI.security import get_current_admin
from shared.models import pacientes, sexos, tipos_diabetes, medicos

router = APIRouter(tags=["CRUD Pacientes"])

# ==================== GET ALL ====================
@router.get("/", response_model=List[PacienteResponse])
def listar_pacientes(
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db),
    medico_id: Optional[int] = Query(None, description="Filtrar por médico"),
    search: Optional[str] = Query(None, description="Buscar por nombre"),
    activos: Optional[bool] = Query(None, description="Solo activos")
):
    """Listar todos los pacientes (solo administradores)"""
    
    query = db.query(pacientes).options(
        joinedload(pacientes.sexo),
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.medico),
        joinedload(pacientes.medico).joinedload(medicos.datos_personales)
    )
    
    if medico_id:
        query = query.filter(pacientes.id_medico == medico_id)
    
    if search:
        query = query.filter(pacientes.nombre_completo.contains(search))
    
    if activos is not None:
        estatus = 1 if activos else 2
        query = query.filter(pacientes.id_estatus_usuario == estatus)
    
    pacientes_list = query.all()
    
    result = []
    for p in pacientes_list:
        edad = date.today().year - p.fecha_nacimiento.year
        medico_nombre = p.medico.datos_personales.nombre_completo if p.medico and p.medico.datos_personales else None
        
        result.append(PacienteResponse(
            id_paciente=p.id_paciente,
            nombre_completo=p.nombre_completo,
            fecha_nacimiento=p.fecha_nacimiento,
            edad=edad,
            sexo=p.sexo.nombre if p.sexo else "No especificado",
            tipo_diabetes=p.tipo_diabetes.nombre if p.tipo_diabetes else None,
            codigo=p.codigo,
            medico_nombre=medico_nombre
        ))
    return result

# ==================== GET BY ID ====================
@router.get("/{paciente_id}", response_model=PacienteResponse)
def obtener_paciente(
    paciente_id: int,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Obtener un paciente por su ID"""
    
    paciente = db.query(pacientes).options(
        joinedload(pacientes.sexo),
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.medico),
        joinedload(pacientes.medico).joinedload(medicos.datos_personales)
    ).filter(pacientes.id_paciente == paciente_id).first()
    
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    edad = date.today().year - paciente.fecha_nacimiento.year
    medico_nombre = paciente.medico.datos_personales.nombre_completo if paciente.medico and paciente.medico.datos_personales else None
    
    return PacienteResponse(
        id_paciente=paciente.id_paciente,
        nombre_completo=paciente.nombre_completo,
        fecha_nacimiento=paciente.fecha_nacimiento,
        edad=edad,
        sexo=paciente.sexo.nombre if paciente.sexo else "No especificado",
        tipo_diabetes=paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
        codigo=paciente.codigo,
        medico_nombre=medico_nombre
    )

# ==================== CREATE ====================
@router.post("/", response_model=PacienteResponse, status_code=status.HTTP_201_CREATED)
def crear_paciente(
    data: PacienteCreate,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Crear un nuevo paciente"""
    
    # Verificar que el médico existe
    medico = db.query(medicos).filter(medicos.id_medico == data.id_medico).first()
    if not medico:
        raise HTTPException(status_code=400, detail="Médico no encontrado")
    
    # Generar código automático
    ultimo = db.query(pacientes).order_by(pacientes.id_paciente.desc()).first()
    if ultimo:
        try:
            num = int(ultimo.codigo.split('-')[-1]) + 1
        except:
            num = db.query(pacientes).count() + 1
    else:
        num = 1
    codigo_generado = f"PAC-{num:04d}"
    
    nuevo_paciente = pacientes(
        id_medico=data.id_medico,
        id_sexo=data.id_sexo,
        id_estatus_usuario=1,
        id_tipo_diabetes=data.id_tipo_diabetes,
        codigo=codigo_generado,
        nombre_completo=data.nombre_completo,
        fecha_nacimiento=data.fecha_nacimiento,
        fecha_hora_registro=datetime.now()
    )
    db.add(nuevo_paciente)
    db.commit()
    db.refresh(nuevo_paciente)
    
    edad = date.today().year - nuevo_paciente.fecha_nacimiento.year
    
    return PacienteResponse(
        id_paciente=nuevo_paciente.id_paciente,
        nombre_completo=nuevo_paciente.nombre_completo,
        fecha_nacimiento=nuevo_paciente.fecha_nacimiento,
        edad=edad,
        sexo=nuevo_paciente.sexo.nombre if nuevo_paciente.sexo else "No especificado",
        tipo_diabetes=nuevo_paciente.tipo_diabetes.nombre if nuevo_paciente.tipo_diabetes else None,
        codigo=nuevo_paciente.codigo,
        medico_nombre=medico.datos_personales.nombre_completo if medico.datos_personales else medico.email
    )

# ==================== UPDATE ====================
@router.put("/{paciente_id}", response_model=PacienteResponse)
def actualizar_paciente(
    paciente_id: int,
    data: PacienteUpdate,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Actualizar un paciente existente"""
    
    paciente = db.query(pacientes).options(
        joinedload(pacientes.sexo),
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.medico),
        joinedload(pacientes.medico).joinedload(medicos.datos_personales)
    ).filter(pacientes.id_paciente == paciente_id).first()
    
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    if data.nombre_completo:
        paciente.nombre_completo = data.nombre_completo
    if data.fecha_nacimiento:
        paciente.fecha_nacimiento = data.fecha_nacimiento
    if data.id_sexo:
        paciente.id_sexo = data.id_sexo
    if data.id_tipo_diabetes is not None:
        paciente.id_tipo_diabetes = data.id_tipo_diabetes
    if data.id_estatus_usuario:
        paciente.id_estatus_usuario = data.id_estatus_usuario
    
    db.commit()
    db.refresh(paciente)
    
    edad = date.today().year - paciente.fecha_nacimiento.year
    medico_nombre = paciente.medico.datos_personales.nombre_completo if paciente.medico and paciente.medico.datos_personales else None
    
    return PacienteResponse(
        id_paciente=paciente.id_paciente,
        nombre_completo=paciente.nombre_completo,
        fecha_nacimiento=paciente.fecha_nacimiento,
        edad=edad,
        sexo=paciente.sexo.nombre if paciente.sexo else "No especificado",
        tipo_diabetes=paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
        codigo=paciente.codigo,
        medico_nombre=medico_nombre
    )

# ==================== DELETE (soft delete) ====================
@router.delete("/{paciente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_paciente(
    paciente_id: int,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Eliminar (desactivar) un paciente"""
    
    paciente = db.query(pacientes).filter(pacientes.id_paciente == paciente_id).first()
    
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    # Soft delete: desactivar en lugar de eliminar
    paciente.id_estatus_usuario = 2
    db.commit()
    
    return None

# ==================== ACTIVAR ====================
@router.patch("/{paciente_id}/activar", response_model=PacienteResponse)
def activar_paciente(
    paciente_id: int,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Activar un paciente desactivado"""
    
    paciente = db.query(pacientes).options(
        joinedload(pacientes.sexo),
        joinedload(pacientes.tipo_diabetes),
        joinedload(pacientes.medico),
        joinedload(pacientes.medico).joinedload(medicos.datos_personales)
    ).filter(pacientes.id_paciente == paciente_id).first()
    
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    paciente.id_estatus_usuario = 1
    db.commit()
    db.refresh(paciente)
    
    edad = date.today().year - paciente.fecha_nacimiento.year
    medico_nombre = paciente.medico.datos_personales.nombre_completo if paciente.medico and paciente.medico.datos_personales else None
    
    return PacienteResponse(
        id_paciente=paciente.id_paciente,
        nombre_completo=paciente.nombre_completo,
        fecha_nacimiento=paciente.fecha_nacimiento,
        edad=edad,
        sexo=paciente.sexo.nombre if paciente.sexo else "No especificado",
        tipo_diabetes=paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
        codigo=paciente.codigo,
        medico_nombre=medico_nombre
    )