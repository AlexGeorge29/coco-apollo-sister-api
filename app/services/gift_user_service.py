from app.models.schemas.gift_user import GiftUserResponse, GiftUsersListResponse
from app.repositories.gift_user_repository import GiftUserRepository
from app.utilse.exceptions import GiftsUserRetrievalError


class GiftUserService:
    def __init__(self):
        self.repository = GiftUserRepository()

    def get_gift_users(self) -> GiftUsersListResponse:
        """Retrieve all gift users and return them in a paginated response."""
        try:
            gift_users = self.repository.get_all()
            return GiftUsersListResponse(gift_users=gift_users)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Erreur lors de la récupération des utilisateurs de cadeaux: {str(e)}"
            ) from e

    def get_gift_user(self, gift_user_id: int) -> GiftUserResponse:
        """Retrieve a specific gift user by ID."""
        try:
            gift_user = self.repository.get_by_id(gift_user_id)
            if not gift_user:
                raise GiftsUserRetrievalError("Gift user not found")
            return gift_user
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Erreur lors de la récupération {gift_user_id}: {str(e)}"
            ) from e

    def get_gift_users_by_user_id(self, user_id: int) -> GiftUsersListResponse:
        """Retrieve gift users by user ID."""
        try:
            gift_users = self.repository.get_by_user_id(user_id)
            if not gift_users:
                raise GiftsUserRetrievalError("No gift users found for this user ID")
            return GiftUsersListResponse(gift_users=gift_users)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Erreur lors de la récupération des utilisateurs de cadeaux pour l'ID utilisateur {user_id}: {str(e)}"
            ) from e
