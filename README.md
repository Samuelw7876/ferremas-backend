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

![image](https://github.com/user-attachments/assets/d3a2372d-fc95-410f-a2f3-02e4a741a3b5)


