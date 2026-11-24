from fastapi import HTTPException

from app.models.herramienta import Herramienta
from app.repositories.herramienta_repository import HerramientaRepository


class HerramientaService:
    def __init__(self, repo: HerramientaRepository):
        self.repo = repo

    def registrar(self, data):
        if self.repo.obtener_por_codigo(data.codigo):
            raise HTTPException(
                status_code=400, detail="Ya existe una herramienta con ese código"
            )

        herramienta = Herramienta(
            nombre=data.nombre,
            codigo=data.codigo,
            categoria=data.categoria,
            marca=data.marca,
            cantidad_disponible=data.cantidad_disponible,
        )
        return self.repo.crear(herramienta)

    def consultar_todas(self, categoria: str | None = None):
        return self.repo.listar(categoria)

    def consultar_por_id(self, herramienta_id: int):
        herramienta = self.repo.obtener_por_id(herramienta_id)
        if herramienta is None:
            raise HTTPException(status_code=404, detail="Herramienta no encontrada")
        return herramienta

    def actualizar(self, herramienta_id: int, data):
        herramienta = self.consultar_por_id(herramienta_id)

        repetida = self.repo.obtener_por_codigo(data.codigo)
        if repetida and repetida.id != herramienta_id:
            raise HTTPException(
                status_code=400, detail="Ya existe una herramienta con ese código"
            )

        herramienta.nombre = data.nombre
        herramienta.codigo = data.codigo
        herramienta.categoria = data.categoria
        herramienta.marca = data.marca
        herramienta.cantidad_disponible = data.cantidad_disponible
        return self.repo.actualizar(herramienta)

    def eliminar(self, herramienta_id: int):
        herramienta = self.consultar_por_id(herramienta_id)
        self.repo.eliminar(herramienta)