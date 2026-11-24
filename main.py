from fastapi import FastAPI

from app.database.conexion import Base, engine
from app.models.usuario import Usuario  # noqa: F401  (para crear la tabla)
from app.models.herramienta import Herramienta  # noqa: F401
from app.routes import usuarios

# Crea las tablas en Neon si todavía no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventario de herramientas")
app.include_router(usuarios.router)