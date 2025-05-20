from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.schemas import UserOut

router = APIRouter(prefix="/api", tags=["protected"])

@router.get("/me")
def read_me(current_user: UserOut = Depends(get_current_user)):
    return {"message": f"Hola {current_user.username}, tu rol es {current_user.role}"}