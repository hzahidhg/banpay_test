# BanPay Test

Repositorio con el proyecto en Python y FastAPI para la prueba técnica de backend de BanPay.

## Requisitos Previos

Para poder ejecutar el proyecto es necesario tener instalado lo siguiente:

- Python 3.11+
- Pip
- PostgreSQL

## Estructura del Proyecto

```bash
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── auth_controller.py  # Definición de controladores de autentificación
│   │   ├── routes.py           # Definición de las rutas del API
│   │   ├── user_controller.py  # Definición de controladores del usuario
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py             # Modelos de roles y del usuario
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── auth.py             # Esquemas para autentificación
│   │   ├── user.py             # Esquemas para user
│   ├── services
│   │   ├── __init__.py
│   │   ├── auth_service.py     # Lógica de servicios de autentificación
│   │   ├── ghibli_service.py   # Lógica se servicios para conectarse Ghibli
│   │   ├── user_service.py     # Lógica de servicios de usuario
│   ├── database.py             # Configuración de la base de datos
│   ├── main.py                 # Archivo main del API
├── requirements.txt            # Dependencias del proyecto
├── migrations                  # Migraciones de base de datos
├── alembic.ini
├── .env.example               
├── .gitignore           
└── README.md                   # Documentación del proyecto
```

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/hzahidhg/banpay_test.git
cd banpay_test
```

2. Crear un entorno virtual y actívarlo:

```bash
python -m venv env
source env/bin/activate
```

3. Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

4. Configurar el archivo .env, crear un archivo .env en la raíz del proyecto y copiar el contenido de .env.example, posterior escribir las variables de tu base de datos, ejemplo:

```bash
DB_USER=user
DB_PASS=pass
DB_HOST=host
DB_PORT=port
DB_NAME=db_name

JWT_SECRET_KEY=SECRET

EXTERNAL_API_URL=https://ghibliapi.vercel.app
```

## Migraciones de Base de Datos

Para poder iniciar el proyecto, es necesario ejecutar las migraciones a la base de datos, con el siguiente comando:

```bash
alembic upgrade head
```

## Ejecución

Para ejecutar el API: 

```bash
uvicorn app.main:app --reload
```

Esto iniciará el servidor de desarrollo en http://127.0.0.1:8000.
