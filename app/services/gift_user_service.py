from app.models.schemas.gift_user import (
    GiftUserResponse,
    GiftUsersListResponse,
    GiftUserToCreate,
    GiftUserToUpdate,
)
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
                f"Erreur pour l'ID utilisateur {user_id}: {str(e)}"
            ) from e

    def get_gift_users_by_gift_id(self, gift_id: int) -> GiftUsersListResponse:
        """Retrieve gift users by gift ID."""
        try:
            gift_users = self.repository.get_by_gift_id(gift_id)
            if not gift_users:
                raise GiftsUserRetrievalError("No gift users found for this gift ID")
            return GiftUsersListResponse(gift_users=gift_users)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Erreur pourpour l'ID cadeau {gift_id}: {str(e)}"
            ) from e

    def create_gift_user(self, gift_user_data: GiftUserToCreate) -> str:
        """Create a new gift user."""
        try:
            gift_user = gift_user_data
            created_gift_user = self.repository.create(gift_user)
            return created_gift_user
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Erreur lors de la création de l'utilisateur de cadeau: {str(e)}"
            ) from e

    def delete_gift_user(self, gift_user_id: int) -> None:
        """Delete a gift user by ID."""
        try:
            self.repository.delete(gift_user_id)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Erreur lors de la suppression ID {gift_user_id}: {str(e)}"
            ) from e

    def update_gift_user(self, gift_user_data: GiftUserToUpdate) -> GiftUserResponse:
        """Update an existing gift user."""
        try:
            updated_gift_user = self.repository.update(gift_user_data)
            return updated_gift_user
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Erreur lors de la mise à jour ID {gift_user_data.id}: {str(e)}"
            ) from e
