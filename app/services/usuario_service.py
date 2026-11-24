import bcrypt
from fastapi import HTTPException

from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def _hashear(self, contrasena: str) -> str:
        return bcrypt.hashpw(
            contrasena.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def registrar(self, data):
        if self.repo.obtener_por_correo(data.correo):
            raise HTTPException(status_code=400, detail="El correo ya está registrado")

        usuario = Usuario(
            nombre=data.nombre,
            correo=data.correo,
            contrasena_hash=self._hashear(data.contrasena),
        )
        return self.repo.crear(usuario)

    def consultar_todos(self):
        return self.repo.listar()

    def consultar_por_id(self, usuario_id: int):
        usuario = self.repo.obtener_por_id(usuario_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario

    def actualizar(self, usuario_id: int, data):
        usuario = self.consultar_por_id(usuario_id)

        repetido = self.repo.obtener_por_correo(data.correo)
        if repetido and repetido.id != usuario_id:
            raise HTTPException(status_code=400, detail="El correo ya está registrado")

        usuario.nombre = data.nombre
        usuario.correo = data.correo
        usuario.contrasena_hash = self._hashear(data.contrasena)
        return self.repo.actualizar(usuario)

    def eliminar(self, usuario_id: int):
        usuario = self.consultar_por_id(usuario_id)
        self.repo.eliminar(usuario)