from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.repositories.herramienta_repository import HerramientaRepository
from app.schemas.herramienta_schema import HerramientaCreate, HerramientaResponse
from app.services.herramienta_service import HerramientaService

router = APIRouter(prefix="/herramientas", tags=["Herramientas"])


def get_service(db: Session = Depends(get_db)):
    return HerramientaService(HerramientaRepository(db))


@router.post("/", response_model=HerramientaResponse, status_code=201)
def registrar(
    data: HerramientaCreate, service: HerramientaService = Depends(get_service)
):
    return service.registrar(data)


# Ejemplo con filtro: /herramientas/?categoria=Manual
@router.get("/", response_model=list[HerramientaResponse])
def consultar_todas(
    categoria: str | None = None,
    service: HerramientaService = Depends(get_service),
):
    return service.consultar_todas(categoria)


@router.get("/{herramienta_id}", response_model=HerramientaResponse)
def consultar_por_id(
    herramienta_id: int, service: HerramientaService = Depends(get_service)
):
    return service.consultar_por_id(herramienta_id)


@router.put("/{herramienta_id}", response_model=HerramientaResponse)
def actualizar(
    herramienta_id: int,
    data: HerramientaCreate,
    service: HerramientaService = Depends(get_service),
):
    return service.actualizar(herramienta_id, data)


@router.delete("/{herramienta_id}", status_code=204)
def eliminar(
    herramienta_id: int, service: HerramientaService = Depends(get_service)
):
    service.eliminar(herramienta_id)