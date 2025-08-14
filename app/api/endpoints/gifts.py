from fastapi import APIRouter, HTTPException
from app.models.schemas.gifts import GiftsListResponse, GiftResponse

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


@router.get("/{gift_id}", response_model=GiftResponse)
def get_gift(gift_id: int):
    """Retrieve a specific gift by ID."""
    try:
        gift = gift_service.get_gift(gift_id)
        if not gift:
            raise HTTPException(status_code=404, detail="Gift not found")
        return gift
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid gift data: {e}") from e
