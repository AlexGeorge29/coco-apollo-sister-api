from pydantic import BaseModel, ConfigDict, field_validator
from app.models.schemas.base import TimestampMixin


class GiftUserBase(BaseModel):

    gift_id: int
    favorite: bool = False
    reserved: bool = False
    bought: bool = False
    user_email: str = ""
    amount: int = 0

    @field_validator("amount")
    @classmethod
    def amount_must_be_non_negative(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Amount must be non-negative")
        return v

    @field_validator("user_email")
    @classmethod
    def email_must_not_be_empty(cls, v: str) -> str:
        if not v:
            raise ValueError("User email must not be empty")
        return v


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
                    "user_email": "cocc@email.com",
                    "favorite": True,
                    "reserved": False,
                    "bought": False,
                    "amount": 10,
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
                        "user_email": "apollo@email.com",
                        "favorite": True,
                        "reserved": False,
                        "bought": False,
                        "amount": 10,
                        "created_at": "2023-10-01T12:00:00Z",
                        "updated_at": "2023-10-01T12:00:00Z",
                    }
                ]
            }
        },
    )


class GiftUserToCreate(GiftUserBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "gift_id": 1,
                "favorite": True,
                "reserved": False,
                "bought": False,
                "amount": 10,
                "user_email": "coco@email.com",
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
