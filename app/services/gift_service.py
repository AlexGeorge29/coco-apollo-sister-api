from app.models.schemas.gifts import GiftsListResponse
from app.repositories.gift_repository import GiftRepository
from app.utilse.exceptions import GiftsRetrievalError


class GiftService:
    def __init__(self):
        self.repository = GiftRepository()

    def get_gifts(self) -> GiftsListResponse:
        """Retrieve all gifts and return them in a paginated response."""
        try:
            gifts = self.repository.get_all()
            return GiftsListResponse(gifts=gifts)
        except Exception as e:
            raise GiftsRetrievalError(
                f"Erreur lors de la récupération des items: {str(e)}"
            ) from e
