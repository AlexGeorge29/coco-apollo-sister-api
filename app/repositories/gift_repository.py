from app.api.helpers.supabase_helpers import SupabaseHelper
from app.database import supabase_client
from app.models.schemas.gifts import GiftModel
from app.utilse.exceptions import GiftsRetrievalError


class GiftRepository:
    def __init__(self):
        self.client = supabase_client.supabase
        self.table = "gifts"

    def get_all(self) -> list[GiftModel]:
        """Retrieve all gifts from the database."""
        try:
            response = SupabaseHelper(self.client, self.table).get_all()
            return [GiftModel(**item) for item in response]
        except Exception as e:
            raise GiftsRetrievalError(
                f"Erreur lors de la récupération des items: {str(e)}"
            ) from e
