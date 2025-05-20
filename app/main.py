from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth_routes, protected_routes

app = FastAPI(title="FERREMAS API Integrada")

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(protected_routes.router)
