from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.models.schemas.base import TimestampMixin


class GiftUserBase(BaseModel):

    gift_id: int
    user_id: UUID
    favorite: bool = False
    reserved: bool = False
    bought: bool = False
    participation: int = 0


class GiftUserResponse(TimestampMixin, GiftUserBase):
    __tablename__ = "gifts_user"

    id: int
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "from_attributes": True,
            "json_schema_extra": {
                "example": {
                    "gift_id": 1,
                    "user_id": "e55b47ca-b8aa-5b81-84b4-75d295e5589z",
                    "favorite": True,
                    "reserved": False,
                    "bought": False,
                }
            },
        },
    )


class GiftUsersListResponse(BaseModel):
    gift_users: list[GiftUserResponse] = []

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "gift_users": [
                    {
                        "id": 1,
                        "gift_id": 1,
                        "user_id": "e55b47ca-b8aa-5b81-84b4-75d295e5589z",
                        "favorite": True,
                        "reserved": False,
                        "bought": False,
                        "created_at": "2023-10-01T12:00:00Z",
                        "updated_at": "2023-10-01T12:00:00Z",
                    }
                ]
            }
        },
    )


class GiftUserToCreate(GiftUserBase):
    email: Optional[str] = ""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "",
                "gift_id": 1,
                "user_id": "e55b47ca-b8aa-5b81-84b4-75d295e5589z",
                "favorite": True,
                "reserved": False,
                "bought": False,
            }
        },
    )


class GiftUserToUpdate(GiftUserBase):
    id: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "gift_id": 1,
                "user_id": "e55b47ca-b8aa-5b81-84b4-75d295e5589z",
                "favorite": True,
                "reserved": False,
                "bought": False,
            }
        },
    )


class GiftUserToDelete(GiftUserBase):
    id: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "gift_id": 1,
                "user_id": "e55b47ca-b8aa-5b81-84b4-75d295e5589z",
                "favorite": True,
                "reserved": False,
                "bought": False,
            }
        },
    )
