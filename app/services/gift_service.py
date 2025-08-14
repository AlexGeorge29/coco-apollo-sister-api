from app.models.schemas.gifts import GiftsListResponse
from app.repositories.gift_repository import GiftRepository


class GiftService:
    def __init__(self):
        self.repository = GiftRepository()

    def get_gifts(self) -> GiftsListResponse:
        """Retrieve all gifts and return them in a paginated response."""
        print("---------------------------------: starting get_gifts")
        gifts = self.repository.get_all()
        print("***************", gifts)
        return GiftsListResponse(gifts=gifts)
