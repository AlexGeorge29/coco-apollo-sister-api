from app.models.schemas.user import UserRegister, RegisterResponse
from app.repositories.user_repository import UserRepository
from app.utilse.exceptions import UserError


class UserService:
    def __init__(self) -> None:
        self.repository = UserRepository()

    def register_user(self, user_data: UserRegister) -> RegisterResponse:
        try:
            return self.repository.create_user(user_data)
        except Exception as e:
            raise UserError(f"Error registering user: {str(e)}") from e
