# 🚀 FERREMAS Backend API

Deberia Funcionar el el railway pero no lo pude probar porque agote el limite mensual, tendrian que probar como hacerlo con la url publica y de momento verlo de manera local.

Este proyecto es una API RESTful desarrollada en **Python + FastAPI**

El objetivo es construir un backend seguro y funcional que permita autenticar usuarios, gestionar roles y consumir servicios externos como la **API base de FERREMAS**, **Stripe** para pagos, y el **Banco Central de Chile** para conversión de moneda.

---

## ✅ Funcionalidades actuales

### 🔐 Autenticación
- Registro de usuarios (`/auth/register`)
- Login con token JWT (`/auth/login`)
- Ruta protegida con token (`/api/me`)

### 🎭 Gestión de roles
- Soporte para roles como: `admin`, `maintainer`, `service_account`
- Base para restringir funcionalidades según permisos

### 🧪 Documentación automática
- Swagger disponible en: `/docs`

---

## 📦 Tecnologías usadas

- **Python 3.11**
- **FastAPI**
- **SQLite + SQLAlchemy**
- **JWT (python-jose)**
- **Passlib (bcrypt)**
- **Swagger UI (OpenAPI)**

---

### 1. Clonar el repositorio

### 2. Crear entorno virtual y activarlo

python -m venv env
pip install -r requirements.txt
uvicorn app.main:app --reload

### 3. Acceder a la API en el navegador
http://127.0.0.1:8000/docs


  ***  Posible orden de lo que se deberia agregar ***

  🗂 Estructura del proyecto

ferremas-backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── roles.py
│   ├── utils.py
│   └── routers/
│       ├── auth_routes.py
│       ├── protected_routes.py
│       ├── productos_routes.py
│       ├── pedidos_routes.py
│       ├── pagos_routes.py
│       ├── monedas_routes.py
│       └── contactos_routes.py
├── requirements.txt
├── Procfile
├── .gitignore![image](https://github.com/user-attachments/assets/033d30af-baf7-4cb3-a6f8-b2be1effae59)


![image](https://github.com/user-attachments/assets/5b30b5f3-13ea-452a-9c49-7c5ab369e6c5)

![image](https://github.com/user-attachments/assets/b27943a4-5266-4731-b91b-94f80623c0f7)

