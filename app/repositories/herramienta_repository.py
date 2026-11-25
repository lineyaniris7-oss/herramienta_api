from sqlalchemy.orm import Session
from app.models.herramienta import Herramienta


class HerramientaRepository:
    def __init__(self, db: Session):
        self.db = db

    def listar(self, categoria: str | None = None):
        consulta = self.db.query(Herramienta)
        if categoria:  # filtro por categoría
            consulta = consulta.filter(Herramienta.categoria.ilike(categoria))
        return consulta.all()

    def obtener_por_id(self, herramienta_id: int):
        return (
            self.db.query(Herramienta)
            .filter(Herramienta.id == herramienta_id)
            .first()
        )

    def obtener_por_codigo(self, codigo: str):
        return (
            self.db.query(Herramienta)
            .filter(Herramienta.codigo == codigo)
            .first()
        )

    def crear(self, herramienta: Herramienta):
        self.db.add(herramienta)
        self.db.commit()
        self.db.refresh(herramienta)
        return herramienta

    def actualizar(self, herramienta: Herramienta):
        self.db.commit()
        self.db.refresh(herramienta)
        return herramienta

    def eliminar(self, herramienta: Herramienta):
        self.db.delete(herramienta)
        self.db.commit()