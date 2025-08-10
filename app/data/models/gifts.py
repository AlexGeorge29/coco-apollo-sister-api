from sqlalchemy import Column, Integer, String, ForeignKey

from app.data.models.base import Base


class Gift(Base):
    __tablename__ = "gifts"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    name: Column[str] = Column(String, nullable=False)
    price: Column[int] = Column(Integer, nullable=False)
    url: Column[str] = Column(String, nullable=False)
    description: Column[str] = Column(String, nullable=True)
    brand: Column[str] = Column(String, nullable=True)
    img_rul: Column[str] = Column(String, nullable=True)
    quantity: Column[int] = Column(Integer, nullable=False, default=1)
    category_id: Column[int] = Column(
        Integer, ForeignKey("categories.id"), nullable=False
    )
    greatings_id: Column[int] = Column(
        Integer, ForeignKey("greatings.id"), nullable=True
    )
    user_id: Column[int] = Column(Integer, ForeignKey("users.id"), nullable=False)
