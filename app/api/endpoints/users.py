from fastapi import APIRouter, HTTPException
from app.models.schemas.user import UserRegister, RegisterResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["users"])
user_service = UserService()


@router.post("/register", response_model=RegisterResponse)
def register(user_data: UserRegister):
    try:
        return user_service.register_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
