# routine4life_mobile/backend/main.py
from fastapi import FastAPI
from shared.database import engine
from shared import models
from routine4life_mobile.backend.routers import pacientes

# Crea las tablas si no existen en SQL Server
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Routine4Life - Mobile API")

# Conectamos nuestras rutas
app.include_router(pacientes.router)

@app.get("/")
def raiz():
    return {"status": "API Móvil en línea"}