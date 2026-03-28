# miAPI/main.py
import sys
import os

# Agregar la carpeta ROUTINE4LIFE al path
project_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from miAPI.routers import medicos_router, pacientes_router

app = FastAPI(
    title="Routine4Life API",
    description="API para gestión de médicos y pacientes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(medicos_router, prefix="/v1/medicos")
app.include_router(pacientes_router, prefix="/v1/pacientes")

@app.get("/")
def root():
    return {
        "message": "Routine4Life API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}