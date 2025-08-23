from fastapi import APIRouter, HTTPException
from app.models.schemas.user import (
    UserLogin,
    UserRegister,
    RegisterResponse,
)
from app.services.user_service import UserService


router = APIRouter(prefix="/auth", tags=["users"])
user_service = UserService()


@router.post("/register", response_model=RegisterResponse)
def register(user_data: UserRegister):
    try:
        return user_service.register_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.post("/login")
def login(credentials: UserLogin):
    try:
        return user_service.get_auth(credentials)
    except Exception as e:
        raise HTTPException(
            status_code=401, detail=f"Authentication failed {str(e)}"
        ) from e
