from app.api.helpers.supabase_helpers import SupabaseHelper
from app.database import supabase_client
from app.models.schemas.gift_user import (
    GiftUserResponse,
    GiftUserToCreate,
    GiftUserToUpdate,
)
from app.utilse.exceptions import GiftsUserRetrievalError


class GiftUserRepository:
    def __init__(self):
        self.client = supabase_client.supabase
        self.table = "gift_users"

    def get_all(self) -> list[GiftUserResponse]:
        """Retrieve all gift users from the database."""
        try:
            response = SupabaseHelper(self.client, self.table).get_all()
            return [GiftUserResponse(**item) for item in response]
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error retrieving gift users: {str(e)}"
            ) from e

    def get_by_id(self, gift_user_id: int) -> GiftUserResponse | None:
        """Retrieve a specific gift user by ID."""
        try:
            response = SupabaseHelper(self.client, self.table).get_by_id(gift_user_id)
            if not response:
                return None
            return GiftUserResponse(**response)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error retrieving gift user with ID {gift_user_id}: {str(e)}"
            ) from e

    def get_by_user_id(self, user_id: int) -> list[GiftUserResponse] | None:
        """Retrieve gift users by user ID."""
        try:
            response = SupabaseHelper(self.client, self.table).get_by_field(
                "user_id", user_id
            )
            if not response:
                return None
            return [GiftUserResponse(**item) for item in response]
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error retrieving gift users for user ID {user_id}: {str(e)}"
            ) from e

    def get_by_gift_id(self, gift_id: int) -> list[GiftUserResponse] | None:
        """Retrieve gift users by gift ID."""
        try:
            response = SupabaseHelper(self.client, self.table).get_by_field(
                "gift_id", gift_id
            )
            if not response:
                return None
            return [GiftUserResponse(**item) for item in response]
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error retrieving gift users for gift ID {gift_id}: {str(e)}"
            ) from e

    def create(self, gift_user: GiftUserToCreate) -> str:
        """Create a new gift user."""
        try:
            data = gift_user.model_dump(exclude_unset=True)
            response = SupabaseHelper(self.client, self.table).create(data)
            if response is None:
                raise GiftsUserRetrievalError("Failed to create gift user")
            return "Gift user created"
        except Exception as e:
            raise GiftsUserRetrievalError(f"Error creating gift user: {str(e)}") from e

    def delete(self, gift_user_id: int) -> None:
        """Delete a gift user by ID."""
        try:
            SupabaseHelper(self.client, self.table).delete(gift_user_id)
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error deleting gift user with ID {gift_user_id}: {str(e)}"
            ) from e

    def update(self, gift_user_data: GiftUserToUpdate) -> GiftUserResponse:
        """Update an existing gift user."""
        try:
            gift_user_id_to_update = gift_user_data.id
            data = gift_user_data.model_dump(exclude_unset=True)
            response = SupabaseHelper(self.client, self.table).update(
                gift_user_id_to_update, data
            )
            if response is None:
                raise GiftsUserRetrievalError("Failed to update gift user")
            return GiftUserResponse(**response)
        except Exception as e:
            raise GiftsUserRetrievalError(f"Error updating gift user  {str(e)}") from e

    def get_gift_user_by_user_email(
        self, user_email: str
    ) -> list[GiftUserResponse] | None:
        """Retrieve gift users by user email."""
        try:
            response = SupabaseHelper(self.client, self.table).get_by_field(
                "user_email", user_email
            )
            if not response:
                return None
            return [GiftUserResponse(**item) for item in response]
        except Exception as e:
            raise GiftsUserRetrievalError(
                f"Error retrieving gift users for user email {user_email}: {str(e)}"
            ) from e
