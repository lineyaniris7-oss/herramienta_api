from pydantic import BaseModel, Field

class HerramientaBase(BaseModel):
    nombre: str
    codigo: str
    categoria: str
    marca: str
    cantidad_disponible: int = Field(ge=0)  # no permite negativos

class HerramientaCrear(HerramientaBase):
    pass

class HerramientaActualizar(HerramientaBase):
    pass

class HerramientaRespuesta(HerramientaBase):
    id: int  # el id solo se devuelve, no se envía al crear

    class Config:
        from_attributes = True