# miAPI/routers/medicos.py
import sys
import os

# Agregar la carpeta ROUTINE4LIFE al path
project_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from datetime import datetime, date
from werkzeug.security import generate_password_hash

from miAPI.data.database import get_db
from miAPI.models.medicosPacientes import MedicoCreate, MedicoUpdate, MedicoResponse
from miAPI.security import get_current_admin
from shared.models import medicos, datos_personales_medico, especialidades_medicas, usuarios

router = APIRouter(tags=["CRUD Médicos"])

@router.get("/", response_model=List[MedicoResponse])
def listar_medicos(
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db),
    activos: Optional[bool] = None
):
    query = db.query(medicos).options(
        joinedload(medicos.datos_personales),
        joinedload(medicos.especialidad)
    ).filter(medicos.id_rol == 2)
    
    if activos is not None:
        estatus = 1 if activos else 2
        query = query.filter(medicos.id_estatus_usuario == estatus)
    
    medicos_list = query.all()
    
    result = []
    for m in medicos_list:
        result.append(MedicoResponse(
            id_medico=m.id_medico,
            nombre_completo=m.datos_personales.nombre_completo,
            email=m.email,
            especialidad=m.especialidad.nombre,
            activo=(m.id_estatus_usuario == 1)
        ))
    return result

@router.get("/{medico_id}", response_model=MedicoResponse)
def obtener_medico(
    medico_id: int,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    medico = db.query(medicos).options(
        joinedload(medicos.datos_personales),
        joinedload(medicos.especialidad)
    ).filter(
        medicos.id_medico == medico_id,
        medicos.id_rol == 2
    ).first()
    
    if not medico:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    
    return MedicoResponse(
        id_medico=medico.id_medico,
        nombre_completo=medico.datos_personales.nombre_completo,
        email=medico.email,
        especialidad=medico.especialidad.nombre,
        activo=(medico.id_estatus_usuario == 1)
    )

@router.post("/", response_model=MedicoResponse, status_code=status.HTTP_201_CREATED)
def crear_medico(
    data: MedicoCreate,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    if db.query(medicos).filter(medicos.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    if db.query(medicos).filter(medicos.rfc == data.rfc).first():
        raise HTTPException(status_code=400, detail="RFC ya registrado")
    
    if db.query(medicos).filter(medicos.cedula_profesional == data.cedula_profesional).first():
        raise HTTPException(status_code=400, detail="Cédula profesional ya registrada")
    
    ultimo = db.query(medicos).order_by(medicos.id_medico.desc()).first()
    if ultimo:
        try:
            num = int(ultimo.codigo.split('-')[-1]) + 1
        except:
            num = db.query(medicos).count() + 1
    else:
        num = 1
    codigo_generado = f"MED-{num:04d}"
    
    datos = datos_personales_medico(
        id_sexo=data.id_sexo,
        id_pais=1,
        nombre_completo=data.nombre_completo,
        fecha_nacimiento=data.fecha_nacimiento,
        telefono=data.telefono,
        fecha_hora_registro=datetime.now()
    )
    db.add(datos)
    db.flush()
    
    nuevo_medico = medicos(
        id_medico=datos.id_medico,
        id_rol=2,
        id_especialidad=data.id_especialidad,
        id_estatus_usuario=1,
        codigo=codigo_generado,
        cedula_profesional=data.cedula_profesional,
        email=data.email,
        rfc=data.rfc
    )
    db.add(nuevo_medico)
    db.flush()
    
    hashed_password = generate_password_hash(data.contrasena)
    nuevo_usuario = usuarios(
        id_rol=2,
        id_medico=nuevo_medico.id_medico,
        id_paciente=None,
        contrasena=hashed_password,
        fecha_registro=date.today()
    )
    db.add(nuevo_usuario)
    db.commit()
    
    especialidad = db.query(especialidades_medicas).filter(
        especialidades_medicas.id_especialidad == data.id_especialidad
    ).first()
    
    return MedicoResponse(
        id_medico=nuevo_medico.id_medico,
        nombre_completo=data.nombre_completo,
        email=data.email,
        especialidad=especialidad.nombre if especialidad else "-",
        activo=True
    )

@router.put("/{medico_id}", response_model=MedicoResponse)
def actualizar_medico(
    medico_id: int,
    data: MedicoUpdate,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    medico = db.query(medicos).options(
        joinedload(medicos.datos_personales),
        joinedload(medicos.especialidad)
    ).filter(
        medicos.id_medico == medico_id,
        medicos.id_rol == 2
    ).first()
    
    if not medico:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    
    if data.nombre_completo:
        medico.datos_personales.nombre_completo = data.nombre_completo
    if data.telefono:
        medico.datos_personales.telefono = data.telefono
    if data.email:
        medico.email = data.email
    if data.rfc:
        medico.rfc = data.rfc
    if data.cedula_profesional:
        medico.cedula_profesional = data.cedula_profesional
    if data.id_especialidad:
        medico.id_especialidad = data.id_especialidad
    if data.id_estatus_usuario:
        medico.id_estatus_usuario = data.id_estatus_usuario
    
    db.commit()
    db.refresh(medico)
    
    return MedicoResponse(
        id_medico=medico.id_medico,
        nombre_completo=medico.datos_personales.nombre_completo,
        email=medico.email,
        especialidad=medico.especialidad.nombre,
        activo=(medico.id_estatus_usuario == 1)
    )

@router.delete("/{medico_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_medico(
    medico_id: int,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    medico = db.query(medicos).filter(
        medicos.id_medico == medico_id,
        medicos.id_rol == 2
    ).first()
    
    if not medico:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    
    medico.id_estatus_usuario = 2
    db.commit()
    
    return None

@router.patch("/{medico_id}/activar", response_model=MedicoResponse)
def activar_medico(
    medico_id: int,
    admin: medicos = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    medico = db.query(medicos).filter(
        medicos.id_medico == medico_id,
        medicos.id_rol == 2
    ).first()
    
    if not medico:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    
    medico.id_estatus_usuario = 1
    db.commit()
    db.refresh(medico)
    
    return MedicoResponse(
        id_medico=medico.id_medico,
        nombre_completo=medico.datos_personales.nombre_completo,
        email=medico.email,
        especialidad=medico.especialidad.nombre,
        activo=True
    )