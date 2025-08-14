from fastapi import APIRouter, HTTPException
from app.models.schemas.gifts import GiftModel

# from app.database.supabase_client import supabase
from app.services.gift_service import GiftService

router = APIRouter(prefix="/gifts", tags=["gifts"])
gift_service = GiftService()


@router.get("/")
def get_gifts():
    """Retrieve all gifts."""
    try:
        return gift_service.get_gifts()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Invalid gift data: {e}") from e
