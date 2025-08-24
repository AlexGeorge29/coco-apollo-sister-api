from app.models.schemas.gifts import GiftResponse, GiftsListResponse
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
            raise GiftsRetrievalError(f"Error in the gifts retrieval: {str(e)}") from e

    def get_gift(self, gift_id: int) -> GiftResponse:
        """Retrieve a specific gift by ID."""
        try:
            gift = self.repository.get_by_id(gift_id)
            if not gift:
                raise GiftsRetrievalError("Gift not found")
            return gift
        except Exception as e:
            raise GiftsRetrievalError(
                f"Error in the retrieval of the gift ID: {gift_id}: {str(e)}"
            ) from e
