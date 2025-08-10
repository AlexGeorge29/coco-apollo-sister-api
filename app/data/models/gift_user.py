from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, ForeignKey, Boolean


class GiftUserBase(BaseModel):

    gift_id = Column(Integer, ForeignKey("gifts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    favorite = Column(Boolean, default=False, nullable=False)
    reserved = Column(Boolean, default=False, nullable=False)
    bouth = Column(Boolean, default=False, nullable=False)


class GiftUser(GiftUserBase):
    __tablename__ = "gifts_user"

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
