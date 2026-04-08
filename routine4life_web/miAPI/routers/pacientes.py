import sys
import os

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

@router.get("/", response_model=dict)
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
        
        result.append({
            "id_paciente": p.id_paciente,
            "nombre_completo": p.nombre_completo,
            "fecha_nacimiento": p.fecha_nacimiento,
            "edad": edad,
            "sexo": p.sexo.nombre if p.sexo else "No especificado",
            "tipo_diabetes": p.tipo_diabetes.nombre if p.tipo_diabetes else None,
            "codigo": p.codigo,
            "medico_nombre": medico_nombre
        })
    
    filtros = []
    if medico_id:
        filtros.append(f"médico ID: {medico_id}")
    if search:
        filtros.append(f"búsqueda: '{search}'")
    if activos is not None:
        filtros.append(f"activos: {activos}")
    
    texto_filtros = f" con filtros ({', '.join(filtros)})" if filtros else ""
    
    return {
        "mensaje": f"Se encontraron {len(result)} paciente(s){texto_filtros}",
        "total": len(result),
        "pacientes": result
    }

@router.get("/{paciente_id}", response_model=dict)
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
    
    return {
        "mensaje": "Paciente encontrado",
        "id_paciente": paciente.id_paciente,
        "nombre_completo": paciente.nombre_completo,
        "fecha_nacimiento": paciente.fecha_nacimiento,
        "edad": edad,
        "sexo": paciente.sexo.nombre if paciente.sexo else "No especificado",
        "tipo_diabetes": paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
        "codigo": paciente.codigo,
        "medico_nombre": medico_nombre,
        "activo": (paciente.id_estatus_usuario == 1)
    }

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
def crear_paciente(
    data: PacienteCreate,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Crear un nuevo paciente"""
    
    medico = db.query(medicos).filter(medicos.id_medico == data.id_medico).first()
    if not medico:
        raise HTTPException(status_code=400, detail="Médico no encontrado")
    
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
    medico_nombre = medico.datos_personales.nombre_completo if medico.datos_personales else medico.email
    
    return {
        "mensaje": f"Paciente registrado exitosamente",
        "id_paciente": nuevo_paciente.id_paciente,
        "nombre_completo": nuevo_paciente.nombre_completo,
        "codigo": codigo_generado,
        "fecha_nacimiento": nuevo_paciente.fecha_nacimiento,
        "edad": edad,
        "sexo": nuevo_paciente.sexo.nombre if nuevo_paciente.sexo else "No especificado",
        "tipo_diabetes": nuevo_paciente.tipo_diabetes.nombre if nuevo_paciente.tipo_diabetes else None,
        "medico_asignado": medico_nombre,
        "activo": True
    }

@router.put("/{paciente_id}", response_model=dict)
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
    
    cambios = []
    nombre_original = paciente.nombre_completo
    
    if data.nombre_completo:
        paciente.nombre_completo = data.nombre_completo
        cambios.append(f"nombre: '{nombre_original}' -> '{data.nombre_completo}'")
    if data.fecha_nacimiento:
        fecha_original = paciente.fecha_nacimiento
        paciente.fecha_nacimiento = data.fecha_nacimiento
        cambios.append(f"fecha de nacimiento: {fecha_original} -> {data.fecha_nacimiento}")
    if data.id_sexo:
        sexo_original = paciente.sexo.nombre if paciente.sexo else "No especificado"
        paciente.id_sexo = data.id_sexo
        nuevo_sexo = db.query(sexos).filter(sexos.id_sexo == data.id_sexo).first()
        cambios.append(f"sexo: {sexo_original} -> {nuevo_sexo.nombre if nuevo_sexo else 'No especificado'}")
    if data.id_tipo_diabetes is not None:
        diabetes_original = paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else "No especificado"
        paciente.id_tipo_diabetes = data.id_tipo_diabetes
        nueva_diabetes = db.query(tipos_diabetes).filter(tipos_diabetes.id_tipo_diabetes == data.id_tipo_diabetes).first()
        cambios.append(f"tipo de diabetes: {diabetes_original} -> {nueva_diabetes.nombre if nueva_diabetes else 'No especificado'}")
    if data.id_estatus_usuario:
        estado_original = "activo" if paciente.id_estatus_usuario == 1 else "inactivo"
        estado_nuevo = "activo" if data.id_estatus_usuario == 1 else "inactivo"
        paciente.id_estatus_usuario = data.id_estatus_usuario
        cambios.append(f"estado: {estado_original} -> {estado_nuevo}")
    
    db.commit()
    db.refresh(paciente)
    
    if not cambios:
        return {
            "mensaje": "No se realizaron cambios",
            "id_paciente": paciente_id,
            "nombre": paciente.nombre_completo
        }
    
    edad = date.today().year - paciente.fecha_nacimiento.year
    medico_nombre = paciente.medico.datos_personales.nombre_completo if paciente.medico and paciente.medico.datos_personales else None
    
    return {
        "mensaje": "Paciente actualizado exitosamente",
        "cambios_realizados": cambios,
        "id_paciente": paciente.id_paciente,
        "nombre_completo": paciente.nombre_completo,
        "codigo": paciente.codigo,
        "fecha_nacimiento": paciente.fecha_nacimiento,
        "edad": edad,
        "sexo": paciente.sexo.nombre if paciente.sexo else "No especificado",
        "tipo_diabetes": paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
        "medico_asignado": medico_nombre,
        "activo": (paciente.id_estatus_usuario == 1)
    }

@router.delete("/{paciente_id}", status_code=status.HTTP_200_OK, response_model=dict)
def eliminar_paciente(
    paciente_id: int,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Eliminar (desactivar) un paciente"""
    
    paciente = db.query(pacientes).filter(pacientes.id_paciente == paciente_id).first()
    
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    nombre_paciente = paciente.nombre_completo
    estado_anterior = "activo" if paciente.id_estatus_usuario == 1 else "inactivo"
    
    paciente.id_estatus_usuario = 2
    db.commit()
    
    return {
        "mensaje": f"Paciente desactivado exitosamente",
        "id_paciente": paciente_id,
        "nombre": nombre_paciente,
        "codigo": paciente.codigo,
        "estado_anterior": estado_anterior,
        "estado_actual": "inactivo (desactivado)",
        "nota": "El paciente ha sido desactivado pero sus datos permanecen en el sistema"
    }

@router.patch("/{paciente_id}/activar", response_model=dict)
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
    
    if paciente.id_estatus_usuario == 1:
        return {
            "mensaje": "El paciente ya estaba activo",
            "id_paciente": paciente_id,
            "nombre": paciente.nombre_completo,
            "codigo": paciente.codigo,
            "estado": "activo"
        }
    
    paciente.id_estatus_usuario = 1
    db.commit()
    db.refresh(paciente)
    
    edad = date.today().year - paciente.fecha_nacimiento.year
    medico_nombre = paciente.medico.datos_personales.nombre_completo if paciente.medico and paciente.medico.datos_personales else None
    
    return {
        "mensaje": f"Paciente activado exitosamente",
        "id_paciente": paciente.id_paciente,
        "nombre": paciente.nombre_completo,
        "codigo": paciente.codigo,
        "fecha_nacimiento": paciente.fecha_nacimiento,
        "edad": edad,
        "sexo": paciente.sexo.nombre if paciente.sexo else "No especificado",
        "tipo_diabetes": paciente.tipo_diabetes.nombre if paciente.tipo_diabetes else None,
        "medico_asignado": medico_nombre,
        "estado_anterior": "inactivo",
        "estado_actual": "activo"
    }