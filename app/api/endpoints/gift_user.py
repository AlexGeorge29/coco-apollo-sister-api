from fastapi import APIRouter, HTTPException
from app.models.schemas.gift_user import (
    GiftUserToUpdate,
    GiftUsersListResponse,
    GiftUserResponse,
    GiftUserToCreate,
)
from app.services.gift_user_service import GiftUserService

router = APIRouter(prefix="/gift_users", tags=["gift_user"])
gift_user_service = GiftUserService()


@router.get("/", response_model=GiftUsersListResponse)
def get_gift_users():
    """Retrieve all gift users."""
    try:
        return gift_user_service.get_gift_users()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving gift users: {e}"
        ) from e


@router.get("/{gift_user_id}", response_model=GiftUserResponse)
def get_gift_user(gift_user_id: int):
    """Retrieve a specific gift user by ID."""
    try:
        gift_user = gift_user_service.get_gift_user(gift_user_id)
        if not gift_user:
            raise HTTPException(status_code=404, detail="Gift user not found")
        return gift_user
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving gift user: {e}"
        ) from e


@router.get("/user/{user_id}", response_model=GiftUsersListResponse)
def get_gift_users_by_user_id(user_id: int):
    """Retrieve gift users by user ID."""
    try:
        return gift_user_service.get_gift_users_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving gift users by user ID: {e}"
        ) from e


@router.get("/gift/{gift_id}", response_model=GiftUsersListResponse)
def get_gift_users_by_gift_id(gift_id: int):
    """Retrieve gift users by gift ID."""
    try:
        return gift_user_service.get_gift_users_by_gift_id(gift_id)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving gift users by gift ID: {e}"
        ) from e


@router.post("/add", response_model=str)
def create_gift_user(gift_user_data: GiftUserToCreate):
    """Create a new gift user."""
    try:
        return gift_user_service.create_gift_user(gift_user_data)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error creating gift user: {e}"
        ) from e


@router.delete("/delete/{gift_user_id}", status_code=204)
def delete_gift_user(gift_user_id: int):
    """Delete a gift user by ID."""
    try:
        gift_user_service.delete_gift_user(gift_user_id)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error deleting gift user: {e}"
        ) from e


@router.put("/update/{gift_user_id}", response_model=GiftUserResponse)
def update_gift_user(gift_user_data: GiftUserToUpdate):
    """Update a gift user by ID."""
    try:
        return gift_user_service.update_gift_user(gift_user_data)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error updating gift user: {e}"
        ) from e
