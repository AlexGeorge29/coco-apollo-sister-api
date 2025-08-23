from app.api.helpers.supabase_helpers import SupabaseHelper
from app.database import supabase_client
from app.models.schemas.gifts import GiftResponse
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
            raise GiftsRetrievalError(
                f"Erreur lors de la récupération des items: {str(e)}"
            ) from e

    def get_by_id(self, gift_id: int) -> GiftResponse | None:
        """Retrieve a specific gift by ID."""
        try:
            response = SupabaseHelper(self.client, self.table).get_by_id(gift_id)
            if not response:
                return None
            return GiftResponse(**response)
        except Exception as e:
            raise GiftsRetrievalError(
                f"Erreur lors de la récupération de l'item avec l'ID {gift_id}: {str(e)}"
            ) from e
