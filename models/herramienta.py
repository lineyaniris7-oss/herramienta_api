from sqlalchemy import Column, Integer, String
from app.database.conexion import Base

class Herramienta(Base):
    __tablename__ = "herramientas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(50), unique=True, nullable=False)
    categoria = Column(String(50), nullable=False)
    marca = Column(String(50), nullable=False)
    cantidad_disponible = Column(Integer, nullable=False)