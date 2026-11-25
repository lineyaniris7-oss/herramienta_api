
from fastapi import FastAPI

from app.database.conexion import Base, engine
from app.models.usuario import Usuario  # noqa: F401
from app.models.herramienta import Herramienta  # noqa: F401
from app.routes import usuarios, herramienta

# Crea las tablas en Neon si todavía no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventario de herramientas")


@app.get("/")
def inicio():
    return {
        "mensaje": "API Inventario de Herramientas funcionando correctamente",
        "estado": "Activa"
    }


app.include_router(usuarios.router)
app.include_router(herramienta.router)
