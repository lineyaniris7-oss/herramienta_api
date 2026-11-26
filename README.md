# API Inventario de Herramientas

API REST para administrar el inventario de herramientas de un taller y los usuarios del sistema. Está desarrollada con FastAPI y PostgreSQL (Neon), utilizando arquitectura por capas.

## Autor

**Line Yaniris Galeano Patiño**

Aprendiz del SENA.

## 1. Objetivo del proyecto

Permitir registrar, consultar, actualizar y eliminar herramientas de un taller, incluyendo la posibilidad de filtrar por categoría. También permite administrar los usuarios del sistema, almacenando sus contraseñas de forma segura mediante hash.

## 2. Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación |
| FastAPI | Construcción de la API REST |
| SQLAlchemy | Comunicación con la base de datos |
| PostgreSQL en Neon | Base de datos en la nube |
| bcrypt | Hash de contraseñas |
| Git y GitHub | Control de versiones |
| Render | Despliegue de la API |

## 3. Módulos desarrollados

### Módulo de Usuarios

Permite registrar, consultar, actualizar y eliminar usuarios. Valida los campos obligatorios, evita correos duplicados y almacena las contraseñas mediante hash bcrypt.

### Módulo de Herramientas

Permite registrar, consultar, actualizar y eliminar herramientas del inventario. También permite filtrar las herramientas por categoría.

Los campos de las herramientas son: nombre, código, categoría, marca y cantidad disponible.

## 4. Arquitectura por capas

El proyecto utiliza una arquitectura por capas que permite separar las responsabilidades y organizar el código.

```mermaid
flowchart TD
    A[Cliente / Swagger] --> B[Routes]
    B --> C[Services]
    C --> D[Repositories]
    D --> E[(Neon PostgreSQL)]
```

La petición pasa por las diferentes capas y la respuesta regresa al cliente.

### Responsabilidad de cada capa

| Capa | Responsabilidad |
|---|---|
| Routes | Define los endpoints y recibe las solicitudes HTTP. |
| Services | Contiene la lógica del negocio y las validaciones correspondientes. |
| Repositories | Ejecuta las operaciones sobre la base de datos. |
| Models | Representa las tablas de PostgreSQL. |
| Schemas | Valida los datos de entrada y salida. |
| Database | Administra la conexión con Neon. |

## 5. Estructura del proyecto

```text
herramienta_api/
├── app/
│   ├── database/
│   │   └── conexion.py
│   ├── models/
│   │   ├── usuario.py
│   │   └── herramienta.py
│   ├── schemas/
│   │   ├── usuario_schema.py
│   │   └── herramienta_schema.py
│   ├── repositories/
│   │   ├── usuario_repository.py
│   │   └── herramienta_repository.py
│   ├── services/
│   │   ├── usuario_service.py
│   │   └── herramienta_service.py
│   └── routes/
│       ├── usuarios.py
│       └── herramienta.py
├── evidencias/
├── main.py
├── requirements.txt
├── .env
└── .gitignore
```

## 6. Base de datos

La aplicación utiliza PostgreSQL alojado en Neon. Se manejan dos tablas independientes, sin relaciones entre ellas.

### Tabla usuarios

| Campo | Tipo | Descripción |
|---|---|---|
| id | Serial (PK) | Identificador único del usuario. |
| nombre | VARCHAR(100) | Nombre completo. |
| correo | VARCHAR(120), UNIQUE | Correo electrónico. |
| contrasena_hash | VARCHAR(255) | Contraseña almacenada mediante hash bcrypt. |

### Tabla herramientas

| Campo | Tipo | Descripción |
|---|---|---|
| id | Serial (PK) | Identificador único de la herramienta. |
| nombre | VARCHAR(100) | Nombre de la herramienta. |
| codigo | VARCHAR(50), UNIQUE | Código de identificación. |
| categoria | VARCHAR(50) | Categoría de la herramienta. |
| marca | VARCHAR(50) | Marca de la herramienta. |
| cantidad_disponible | INTEGER | Unidades disponibles. |

### Diagrama de las tablas

```mermaid
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
```

Las tablas son independientes y no tienen relaciones entre sí.

## 7. Endpoints implementados

### Usuarios

| Método | Endpoint | Funcionalidad |
|---|---|---|
| POST | `/usuarios/` | Registrar usuario. |
| GET | `/usuarios/` | Consultar usuarios. |
| GET | `/usuarios/{id}` | Consultar usuario por ID. |
| PUT | `/usuarios/{id}` | Actualizar usuario. |
| DELETE | `/usuarios/{id}` | Eliminar usuario. |

### Herramientas

| Método | Endpoint | Funcionalidad |
|---|---|---|
| POST | `/herramientas/` | Registrar herramienta. |
| GET | `/herramientas/` | Consultar herramientas. |
| GET | `/herramientas/?categoria=Manual` | Filtrar por categoría. |
| GET | `/herramientas/{id}` | Consultar herramienta por ID. |
| PUT | `/herramientas/{id}` | Actualizar herramienta. |
| DELETE | `/herramientas/{id}` | Eliminar herramienta. |

## 8. Códigos de respuesta

| Código | Significado |
|---|---|
| 200 | Consulta o actualización correcta. |
| 201 | Registro creado correctamente. |
| 204 | Eliminación exitosa. |
| 400 | Correo o código duplicado. |
| 404 | Registro no encontrado. |
| 422 | Datos inválidos. |

## 9. Evidencias de pruebas en Swagger

Se realizaron pruebas de los endpoints mediante Swagger UI para comprobar el funcionamiento de las operaciones CRUD de los módulos Usuarios y Herramientas.

### 9.1. Módulo Usuarios

**Registro de usuario (POST)**

![Registro de usuario - Datos](evidencias/cap_u/postdatos.jfif)
![Registro de usuario - Resultados](evidencias/cap_u/postresultados.jfif)

**Consulta de usuarios (GET)**

![Consulta de usuarios - Datos](evidencias/cap_u/getusuariosdatos.jfif)
![Consulta de usuarios - Resultados](evidencias/cap_u/getusuariosresultados.jfif)

**Consulta de usuario por ID (GET)**

![Consulta de usuario por ID - Datos](evidencias/cap_u/getiddatos.jfif)
![Consulta de usuario por ID - Resultados](evidencias/cap_u/getidresultados.jfif)

**Actualización de usuario (PUT)**

![Actualización de usuario - Datos](evidencias/cap_u/putdatos.jfif)
![Actualización de usuario - Resultados](evidencias/cap_u/putresultado.jfif)

**Eliminación de usuario (DELETE)**

![Eliminación de usuario](evidencias/cap_u/deletedatos.jfif)

**Verificación de eliminación (GET)**

![Verificación de eliminación - Datos](evidencias/cap_u/getevidenciaeliminaciondatos.jfif)
![Verificación de eliminación - Resultados](evidencias/cap_u/getevidenciaeliminacionresultado.jfif)

### 9.2. Módulo Herramientas

**Registro de herramienta (POST)**

![Registro de herramienta - Datos](evidencias/cap_h/postdatos.jfif)
![Registro de herramienta - Resultados](evidencias/cap_h/postresultado.jfif)

**Consulta de herramientas (GET)**

![Consulta de herramientas - Datos](evidencias/cap_h/getherramientasdatos.jfif)
![Consulta de herramientas - Resultados](evidencias/cap_h/getherramientasresultados.jfif)

**Consulta de herramienta por ID (GET)**

![Consulta de herramienta por ID - Datos](evidencias/cap_h/getiddatos.jfif)
![Consulta de herramienta por ID - Resultados](evidencias/cap_h/getidresultados.jfif)

**Actualización de herramienta (PUT)**

![Actualización de herramienta - Datos](evidencias/cap_h/putdatos.jfif)
![Actualización de herramienta - Resultados](evidencias/cap_h/putresultado.jfif)

**Eliminación de herramienta (DELETE)**

![Eliminación de herramienta](evidencias/cap_h/deletedatos.jfif)

**Verificación de eliminación (GET)**

![Verificación de eliminación - Datos](evidencias/cap_h/getevidenciaeliminaciondatos.jfif)
![Verificación de eliminación - Resultados](evidencias/cap_h/getevidenciaeliminacionresultado.jfif)

Las pruebas permitieron comprobar el registro, consulta, actualización y eliminación de los datos en ambos módulos.

## 10. Conexión con Neon

La API se conecta a PostgreSQL mediante SQLAlchemy. La dirección de conexión se configura utilizando la variable de entorno `DATABASE_URL`, almacenada localmente en el archivo `.env`.

Este archivo no se publica en GitHub porque contiene información privada de conexión a la base de datos.

En el despliegue de Render, la variable `DATABASE_URL` se configura directamente en las variables de entorno del servicio.

## 11. Ejecución local del proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/lineyaniris7-oss/herramienta_api.git
```

2. Entrar a la carpeta:

```bash
cd herramienta_api
```

3. Crear el entorno virtual:

```bash
python -m venv .venv
```

4. Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

5. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

6. Crear el archivo `.env` en la raíz del proyecto y configurar la conexión:

```env
DATABASE_URL=postgresql://usuario:clave@host/basededatos
```

7. Iniciar el servidor:

```bash
uvicorn main:app --reload
```

8. Abrir Swagger en el navegador:

`http://127.0.0.1:8000/docs`

## 12. Despliegue en Render

La API fue desplegada utilizando Render, conectando el repositorio de GitHub y configurando las variables de entorno necesarias.

### 12.1. Servicio desplegado en Render

Captura del panel de Render donde se muestra el servicio `herramienta-api` con estado activo.

![Servicio desplegado en Render](evidencias/cap_r/servicio_desplegado_en_render.jfif)

### 12.2. API funcionando en línea

Respuesta de la ruta principal de la API, mostrando que el servicio está funcionando correctamente.

![API funcionando](evidencias/cap_r/API_funcionando_en_línea.jfif)

### 12.3. Documentación Swagger en Render

Documentación interactiva de la API desplegada, donde se visualizan los endpoints de usuarios y herramientas.

![Swagger en Render - Usuarios](evidencias/cap_r/Swagger_en_Render_usuarios.jfif)
![Swagger en Render - Herramientas](evidencias/cap_r/Swagger_en_Render_herramientas.jfif)



**Configuración de despliegue:**

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Variable de entorno: `DATABASE_URL`

**URL de la API:**

https://herramienta-api.onrender.com

**Documentación Swagger:**

https://herramienta-api.onrender.com/docs

## 13. Repositorio GitHub

El código fuente del proyecto se encuentra disponible en el siguiente repositorio:

https://github.com/lineyaniris7-oss/herramienta_api