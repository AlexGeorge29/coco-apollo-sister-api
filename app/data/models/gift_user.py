from sqlalchemy import Column, Integer, ForeignKey, Boolean

from app.data.models.base import Base


class GiftUser(Base):
    __tablename__ = "gifts_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    gift_id = Column(Integer, ForeignKey("gifts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    favorite = Column(Boolean, default=False, nullable=False)
    reserved = Column(Boolean, default=False, nullable=False)
    bouth = Column(Boolean, default=False, nullable=False)
