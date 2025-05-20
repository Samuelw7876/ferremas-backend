from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth_routes, protected_routes
from fastapi.responses import RedirectResponse

app = FastAPI(title="FERREMAS API Integrada")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(protected_routes.router)
