from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def get_service(db: Session = Depends(get_db)):
    return UsuarioService(UsuarioRepository(db))


@router.post("/", response_model=UsuarioResponse, status_code=201)
def registrar(data: UsuarioCreate, service: UsuarioService = Depends(get_service)):
    return service.registrar(data)


@router.get("/", response_model=list[UsuarioResponse])
def consultar_todos(service: UsuarioService = Depends(get_service)):
    return service.consultar_todos()


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def consultar_por_id(usuario_id: int, service: UsuarioService = Depends(get_service)):
    return service.consultar_por_id(usuario_id)


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar(
    usuario_id: int,
    data: UsuarioCreate,
    service: UsuarioService = Depends(get_service),
):
    return service.actualizar(usuario_id, data)


@router.delete("/{usuario_id}", status_code=204)
def eliminar(usuario_id: int, service: UsuarioService = Depends(get_service)):
    service.eliminar(usuario_id)