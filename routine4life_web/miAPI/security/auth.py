# miAPI/security/auth.py
import sys
import os

project_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash

from miAPI.data.database import get_db
from shared.models import usuarios, medicos

security = HTTPBasic()

def get_current_admin(
    credentials: HTTPBasicCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    medico = db.query(medicos).filter(
        medicos.email == credentials.username
    ).first()
    
    if not medico:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    usuario = db.query(usuarios).filter(
        usuarios.id_medico == medico.id_medico
    ).first()
    
    if not usuario or not check_password_hash(usuario.contrasena, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    if medico.id_rol != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requieren permisos de administrador"
        )
    
    return medico