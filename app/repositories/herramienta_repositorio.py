from sqlalchemy.orm import Session
from app.models.herramienta import Herramienta

class HerramientaRepository:
    def __init__(self, db: Session):
        self.db = db

    def crear(self, datos: dict):
        herramienta = Herramienta(**datos)
        self.db.add(herramienta)
        self.db.commit()
        self.db.refresh(herramienta)
        return herramienta

    def listar(self, categoria: str | None = None):
        consulta = self.db.query(Herramienta)
        if categoria:  # aquí va el filtro (actividad 5)
            consulta = consulta.filter(Herramienta.categoria.ilike(categoria))
        return consulta.all()

    def obtener_por_id(self, id: int):
        return self.db.query(Herramienta).filter(Herramienta.id == id).first()

    def obtener_por_codigo(self, codigo: str):
        return self.db.query(Herramienta).filter(Herramienta.codigo == codigo).first()

    def actualizar(self, herramienta, datos: dict):
        for campo, valor in datos.items():
            setattr(herramienta, campo, valor)
        self.db.commit()
        self.db.refresh(herramienta)
        return herramienta

    def eliminar(self, herramienta):
        self.db.delete(herramienta)
        self.db.commit()