from app.models.schemas.gift_user import (
    GiftUserResponse,
    GiftUsersListResponse,
    GiftUserToCreate,
    GiftUserToUpdate,
)
from app.repositories.gift_user_repository import GiftUserRepository
from app.utilse.exceptions import GiftsUserRetrievalError
from app.services.gift_service import GiftService
from app.models.schemas.gifts import GiftToUpdate


class GiftUserService:
    def __init__(self):
        self.repository = GiftUserRepository()
        self.gift_service = GiftService()

    def get_gift_users(self) -> GiftUsersListResponse:
        """Retrieve all gift users and return them in a paginated response."""
        try:
            gift_users = self.repository.get_all()
            return GiftUsersListResponse(gift_users=gift_users)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error retrieving gift users: {str(e)}"
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
                f"Error retrieving gift_user id: {gift_user_id}: {str(e)}"
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
                f"Error retrieval gift_user for gift id: {gift_id}: {str(e)}"
            ) from e

    def create_gift_user(self, gift_user_data: GiftUserToCreate) -> str:
        """Create a new gift user."""
        try:
            gift_user = gift_user_data
            gift = self.gift_service.get_gift(gift_user.gift_id)
            if gift_user.amount > gift.remaining_amount:
                raise GiftsUserRetrievalError(
                    "Insufficient remaining amount in the gift"
                )
            gift.remaining_amount -= gift_user.amount
            self.gift_service.update_gift(
                gift.id, GiftToUpdate(**gift.model_dump(exclude_unset=True))
            )
            created_gift_user = self.repository.create(gift_user)
            return created_gift_user
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error in he creation of gift_user: {str(e)}"
            ) from e

    def delete_gift_user(self, gift_user_id: int) -> None:
        """Delete a gift user by ID."""
        try:
            self.repository.delete(gift_user_id)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error in the deletion of gift_user id: {gift_user_id}: {str(e)}"
            ) from e

    def update_gift_user(self, gift_user_data: GiftUserToUpdate) -> GiftUserResponse:
        """Update an existing gift user."""
        try:
            updated_gift_user = self.repository.update(gift_user_data)
            return updated_gift_user
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error in the update of gift_user id: {gift_user_data.id}: {str(e)}"
            ) from e

    def get_gift_users_by_user_email(self, user_email: str) -> GiftUsersListResponse:
        """Retrieve gift users by user email."""
        try:
            gift_users = self.repository.get_gift_user_by_user_email(user_email)
            if not gift_users:
                raise GiftsUserRetrievalError("No gift users found for this user email")
            return GiftUsersListResponse(gift_users=gift_users)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error retrieval gift_user for user email: {user_email}: {str(e)}"
            ) from e
