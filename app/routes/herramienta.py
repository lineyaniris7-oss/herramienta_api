from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.models.herramienta import Herramienta
from app.schemas.herramienta_schema import HerramientaCreate, HerramientaResponse

router = APIRouter(prefix="/herramientas", tags=["Herramientas"])


# GET: Consultar todas (filtro opcional por categoría)
@router.get("/", response_model=list[HerramientaResponse])
def get_herramientas(
    categoria: str | None = None,
    db: Session = Depends(get_db)
):
    consulta = db.query(Herramienta)

    if categoria:
        consulta = consulta.filter(
            Herramienta.categoria.ilike(categoria)
        )

    return consulta.all()


# GET: Consultar una herramienta por ID
@router.get("/{herramienta_id}", response_model=HerramientaResponse)
def get_herramienta(
    herramienta_id: int,
    db: Session = Depends(get_db)
):
    herramienta = db.query(Herramienta).filter(
        Herramienta.id == herramienta_id
    ).first()

    if herramienta is None:
        raise HTTPException(
            status_code=404,
            detail="Herramienta no encontrada"
        )

    return herramienta


# POST: Registrar una herramienta
@router.post("/", response_model=HerramientaResponse, status_code=201)
def create_herramienta(
    data: HerramientaCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(Herramienta).filter(
        Herramienta.codigo == data.codigo
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una herramienta con ese código"
        )

    herramienta = Herramienta(
        nombre=data.nombre,
        codigo=data.codigo,
        categoria=data.categoria,
        marca=data.marca,
        cantidad_disponible=data.cantidad_disponible
    )

    db.add(herramienta)
    db.commit()
    db.refresh(herramienta)

    return herramienta


# PUT: Actualizar una herramienta
@router.put("/{herramienta_id}", response_model=HerramientaResponse)
def update_herramienta(
    herramienta_id: int,
    data: HerramientaCreate,
    db: Session = Depends(get_db)
):
    herramienta = db.query(Herramienta).filter(
        Herramienta.id == herramienta_id
    ).first()

    if herramienta is None:
        raise HTTPException(
            status_code=404,
            detail="Herramienta no encontrada"
        )

    duplicated = db.query(Herramienta).filter(
        Herramienta.codigo == data.codigo,
        Herramienta.id != herramienta_id
    ).first()

    if duplicated:
        raise HTTPException(
            status_code=400,
            detail="Ya existe una herramienta con ese código"
        )

    herramienta.nombre = data.nombre
    herramienta.codigo = data.codigo
    herramienta.categoria = data.categoria
    herramienta.marca = data.marca
    herramienta.cantidad_disponible = data.cantidad_disponible

    db.commit()
    db.refresh(herramienta)

    return herramienta


# DELETE: Eliminar una herramienta
@router.delete("/{herramienta_id}")
def delete_herramienta(
    herramienta_id: int,
    db: Session = Depends(get_db)
):
    herramienta = db.query(Herramienta).filter(
        Herramienta.id == herramienta_id
    ).first()

    if herramienta is None:
        raise HTTPException(
            status_code=404,
            detail="Herramienta no encontrada"
        )

    db.delete(herramienta)
    db.commit()

    return {"message": "Herramienta eliminada correctamente"}