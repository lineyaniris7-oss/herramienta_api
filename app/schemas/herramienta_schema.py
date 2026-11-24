from pydantic import BaseModel, ConfigDict, Field


class HerramientaCreate(BaseModel):
    nombre: str = Field(min_length=1)
    codigo: str = Field(min_length=1)
    categoria: str = Field(min_length=1)
    marca: str = Field(min_length=1)
    cantidad_disponible: int = Field(ge=0)  # no permite negativos


class HerramientaResponse(HerramientaCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)