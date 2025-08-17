from pydantic import BaseModel, ConfigDict

from app.models.schemas.base import TimestampMixin


class GiftUserBase(BaseModel):

    gift_id: int
    user_id: int
    favorite: bool = False
    reserved: bool = False
    bougth: bool = False


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
                    "user_id": 1,
                    "favorite": True,
                    "reserved": False,
                    "bouth": False,
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
                        "user_id": 1,
                        "favorite": True,
                        "reserved": False,
                        "bouth": False,
                        "created_at": "2023-10-01T12:00:00Z",
                        "updated_at": "2023-10-01T12:00:00Z",
                    }
                ]
            }
        },
    )

    class GiftUserCreate(GiftUserBase):
        id: int
        model_config = ConfigDict(
            json_schema_extra={
                "example": {
                    "gift_id": 1,
                    "user_id": 1,
                    "favorite": True,
                    "reserved": False,
                    "bouth": False,
                }
            },
        )

    class GiftUserUpdate(GiftUserBase):
        id: int

        model_config = ConfigDict(
            json_schema_extra={
                "example": {
                    "id": 1,
                    "gift_id": 1,
                    "user_id": 1,
                    "favorite": True,
                    "reserved": False,
                    "bouth": False,
                }
            },
        )


class GiftUserDelete(GiftUserBase):
    id: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "gift_id": 1,
                "user_id": 1,
                "favorite": True,
                "reserved": False,
                "bouth": False,
            }
        },
    )
