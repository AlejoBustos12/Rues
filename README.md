
# 🚀 FastAPI Bot - Gestión de Tareas con PostgreSQL

Este proyecto es una API construida con **FastAPI** para gestionar tareas de forma eficiente.  
Está conectada a una base de datos **PostgreSQL**, y sigue buenas prácticas de desarrollo con una arquitectura modular.

---

## 📂 **Estructura del Proyecto**
```
app/
│
├── api/
│   └── v1.py          # Endpoints para la gestión de tareas
│
├── core/
│   └── config.py          # Gestion de variables de entorno y globales
│
├── db/
│   ├── database.py       # Configuración y conexión a la base de datos
│   └── models.py         # Modelos SQLAlchemy
│
├── schemas/
│   └── company.py           # Esquemas de validación con Pydantic
│
├── services/
│   └── crud.py           # Metodos que aplican la logica de negocio
│
├── test/
│   └── test_api.py           # Pruebas unitarias
│
├── main.py               # Punto de entrada de la aplicación
│
├── .env                  # Variables de entorno
│
└── requirements.txt      # Dependencias del proyecto
```

---

## ⚙ **Requisitos Previos**

Antes de iniciar, asegúrate de tener instalados:

- [Python 3.9+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)
- [pip](https://pip.pypa.io/en/stable/installation/)

---

## 🔧 **Instalación y Configuración**

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/AlejoBustos12/Rues.git
cd Rues
```


### 2️⃣ Crear y activar un entorno virtual
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / MacOS
.venv\Scripts\activate    # Windows
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```
DATABASE_URL=postgresql+psycopg2://usuario:contraseña@localhost:5432/nombre_base_datos
CORS_ORIGIN=*
API_KEY= api-key-usuario
```

---

## ▶ **Ejecución del servidor**

Para levantar el servidor de desarrollo:
```bash
uvicorn app.main:app --reload
```

Accede a la documentación interactiva en:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📦 **Comandos útiles**

| Comando | Descripción |
|----------|------------|
| `uvicorn app.main:app --reload` | Ejecutar el servidor en modo desarrollo |
| `alembic revision --autogenerate -m "mensaje"` | Crear una nueva migración |
| `alembic upgrade head` | Aplicar migraciones pendientes |
| `alembic downgrade -1` | Revertir la última migración |
---

## 🧪 **Pruebas**
```bash
pytest --maxfail=1 --disable-warnings -q
```

---


## 🛠 **Stack Tecnológico**
- **FastAPI** - Framework backend moderno y rápido
- **PostgreSQL** - Base de datos relacional robusta
- **SQLAlchemy** - ORM para interactuar con la base de datos
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor ASGI para desarrollo

---
**Desarrollado por [Jonathan Alejandro Bustos](https://github.com/AlejoBustos12)**
