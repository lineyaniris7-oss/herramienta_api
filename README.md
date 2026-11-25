# API Inventario de herramientas

API REST para administrar el inventario de herramientas de un taller y los usuarios del sistema. Está desarrollada con FastAPI y PostgreSQL (Neon), usando arquitectura por capas.

## Autor

Line Yaniris Galeano Patiño, aprendiz del SENA.

## Objetivo de la API

Permitir registrar, consultar, actualizar y eliminar herramientas de un taller (con filtro por categoría), y administrar usuarios guardando sus contraseñas de forma segura mediante hash.

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación |
| FastAPI | Construcción de la API REST |
| SQLAlchemy | Comunicación con la base de datos |
| PostgreSQL en Neon | Base de datos en la nube |
| bcrypt | Hash de contraseñas |
| Git / GitHub | Control de versiones |
| Render | Despliegue de la API |

## Módulos desarrollados

- **Usuarios:** CRUD completo. Valida campos obligatorios, evita correos duplicados y guarda la contraseña con hash (nunca en texto plano).
- **Herramientas:** CRUD completo con filtro por categoría.

## Arquitectura por capas

```mermaid
flowchart LR
    C[Cliente / Swagger] --> R[Routes]
    R --> S[Services]
    S --> RP[Repositories]
    RP --> DB[(Neon PostgreSQL)]
```

La petición baja por las capas y la respuesta vuelve por el mismo camino.

### Estructura del proyecto

```
herramienta_api/
├── app/
│   ├── database/       conexion.py
│   ├── models/         usuario.py, herramienta.py
│   ├── schemas/        usuario_schema.py, herramienta_schema.py
│   ├── repositories/   usuario_repository.py, herramienta_repository.py
│   ├── services/       usuario_service.py, herramienta_service.py
│   └── routes/         usuarios.py, herramienta.py
├── main.py
├── requirements.txt
├── .env            
└── .gitignore
```

### Responsabilidad de cada capa

| Capa | Responsabilidad |
|---|---|
| Routes | Definir los endpoints y recibir las solicitudes. |
| Services | Aplicar la lógica del negocio (correo o código repetido, registro no encontrado, hash de contraseña). |
| Repositories | Ejecutar las operaciones sobre la base de datos. |
| Models | Representar las tablas de PostgreSQL. |
| Schemas | Validar los datos de entrada y de salida. |
| Database | Administrar la conexión con Neon. |

## Base de datos

Se utilizan dos tablas independientes (sin relaciones entre ellas).

### Tabla `usuarios`

| Campo | Tipo | Descripción |
|---|---|---|
| id | serial (PK) | Identificador único |
| nombre | varchar(100) | Nombre completo |
| correo | varchar(120), único | Correo electrónico |
| contrasena_hash | varchar(255) | Contraseña almacenada con hash bcrypt |

### Tabla `herramientas`

| Campo | Tipo | Descripción |
|---|---|---|
| id | serial (PK) | Identificador único |
| nombre | varchar(100) | Nombre de la herramienta |
| codigo | varchar(50), único | Código de la herramienta |
| categoria | varchar(50) | Categoría (por ejemplo, Manual o Eléctrica) |
| marca | varchar(50) | Marca |
| cantidad_disponible | integer | Unidades disponibles (no puede ser negativa) |

## Endpoints

### Usuarios

| Método | Endpoint | Funcionalidad |
|---|---|---|
| POST | /usuarios/ | Registrar usuario |
| GET | /usuarios/ | Consultar usuarios |
| GET | /usuarios/{id} | Consultar usuario por ID |
| PUT | /usuarios/{id} | Actualizar usuario |
| DELETE | /usuarios/{id} | Eliminar usuario |

### Herramientas

| Método | Endpoint | Funcionalidad |
|---|---|---|
| POST | /herramientas/ | Registrar herramienta |
| GET | /herramientas/ | Consultar todas las herramientas |
| GET | /herramientas/?categoria=Manual | Filtrar por categoría |
| GET | /herramientas/{id} | Consultar herramienta por ID |
| PUT | /herramientas/{id} | Actualizar herramienta |
| DELETE | /herramientas/{id} | Eliminar herramienta |

### Diagrama de las tablas

```
    USUARIOS {
        int id PK
        string nombre
        string correo UK
        string contrasena_hash
    }
    HERRAMIENTAS {
        int id PK
        string nombre
        string codigo UK
        string categoria
        string marca
        int cantidad_disponible
    }
```

Las dos tablas son independientes, sin relaciones entre ellas.

### Diagrama de las tablas


erDiagram
    USUARIOS {
        int id PK
        string nombre
        string correo UK
        string contrasena_hash
    }
    HERRAMIENTAS {
        int id PK
        string nombre
        string codigo UK
        string categoria
        string marca
        int cantidad_disponible
    }


Las dos tablas son independientes, sin relaciones entre ellas.

### Códigos de respuesta

| Código | Significado |
|---|---|
| 200 | Consulta o actualización correcta |
| 201 | Registro creado |
| 204 | Eliminado correctamente |
| 400 | Correo o código duplicado |
| 404 | Registro no encontrado |
| 422 | Datos inválidos |

## Conexión con Neon

La API se conecta a PostgreSQL en Neon con SQLAlchemy. La URL de conexión se guarda en una variable de entorno (`DATABASE_URL`) dentro del archivo `.env`, que no se publica en GitHub. Al iniciar, `main.py` crea las tablas si todavía no existen.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/herramienta_api.git
   cd herramienta_api
   ```
2. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Crear un archivo `.env` en la raíz con la conexión de Neon:
   ```
   DATABASE_URL=postgresql://usuario:clave@host/basededatos
   ```
5. Iniciar el servidor:
   ```bash
   uvicorn main:app --reload
   ```
6. Abrir la documentación en `http://127.0.0.1:8000/docs`

## Despliegue en Render

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Variable de entorno: `DATABASE_URL`

URL de la API: https://TU-API.onrender.com
Documentación: https://TU-API.onrender.com/docs

## Enlaces

URL de la API: https://herramienta-api.onrender.com
Documentación: https://herramienta-api.onrender.com/docs
Repositorio: https://github.com/lineyaniris7-oss/herramienta_api