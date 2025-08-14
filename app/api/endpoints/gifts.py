from fastapi import APIRouter, HTTPException
from app.models.schemas.gifts import GiftsListResponse

from app.services.gift_service import GiftService

router = APIRouter(prefix="/gifts", tags=["gifts"])
gift_service = GiftService()


@router.get("/", response_model=GiftsListResponse)
def get_gifts():
    """Retrieve all gifts."""
    try:
        return gift_service.get_gifts()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid gift data: {e}") from e
