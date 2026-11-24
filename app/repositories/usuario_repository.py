from sqlalchemy.orm import Session
from app.models.usuario import Usuario


class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(Usuario).all()

    def obtener_por_id(self, usuario_id: int):
        return self.db.query(Usuario).filter(Usuario.id == usuario_id).first()

    def obtener_por_correo(self, correo: str):
        return self.db.query(Usuario).filter(Usuario.correo == correo).first()

    def crear(self, usuario: Usuario):
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def actualizar(self, usuario: Usuario):
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def eliminar(self, usuario: Usuario):
        self.db.delete(usuario)
        self.db.commit()