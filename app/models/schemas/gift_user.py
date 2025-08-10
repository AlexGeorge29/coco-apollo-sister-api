from pydantic import BaseModel, ConfigDict


class GiftUserBase(BaseModel):

    gift_id: int
    user_id: int
    favorite: bool = False
    reserved: bool = False
    bouth: bool = False


class GiftUser(GiftUserBase):
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
