from app.database import supabase_client
from app.models.schemas.user import UserRegister, RegisterResponse
from app.utilse.exceptions import UserError


class UserRepository:
    def __init__(self) -> None:
        self.client = supabase_client.supabase
        self.table = "users"
        if self.client is None:
            raise ValueError("Supabase client is not initialized")

    def create_user(self, user_data: UserRegister) -> RegisterResponse:
        if self.client is None:
            raise ValueError("Supabase client is not initialized")
        try:
            response = self.client.auth.sign_up(
                {"email": user_data.email, "password": user_data.password}
            )
            return RegisterResponse(
                user_id=response.user.id if response.user else None,
                message="Registration successful",
            )
        except Exception as e:
            raise UserError(f"Error creating user: {str(e)}") from e
