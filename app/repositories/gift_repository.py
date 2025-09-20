from app.api.helpers.supabase_helpers import SupabaseHelper
from app.database import supabase_client
from app.models.schemas.gifts import GiftResponse, GiftToUpdate
from app.utilse.exceptions import GiftsRetrievalError


class GiftRepository:
    def __init__(self):
        self.client = supabase_client.supabase
        self.table = "gifts"

    def get_all(self) -> list[GiftResponse]:
        """Retrieve all gifts from the database."""
        try:
            response = SupabaseHelper(self.client, self.table).get_all()
            return [GiftResponse(**item) for item in response]
        except Exception as e:
            raise GiftsRetrievalError(f"Error in the gifts retrieval: {str(e)}") from e

    def get_by_id(self, gift_id: int) -> GiftResponse | None:
        """Retrieve a specific gift by ID."""
        try:
            response = SupabaseHelper(self.client, self.table).get_by_id(gift_id)
            if not response:
                return None
            return GiftResponse(**response)
        except Exception as e:
            raise GiftsRetrievalError(
                f"Error in the gift retrieval ID: {gift_id}: {str(e)}"
            ) from e

    def update(self, gift_id: int, gift_data: GiftToUpdate) -> GiftResponse | None:
        """Update an existing gift."""
        try:
            response = SupabaseHelper(self.client, self.table).update(
                gift_id, gift_data.model_dump(exclude_unset=True)
            )
            if not response:
                return None
            return GiftResponse(**response)
        except Exception as e:
            raise GiftsRetrievalError(
                f"Error updating gift ID: {gift_id}: {str(e)}"
            ) from e
