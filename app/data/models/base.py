from pydantic import BaseModel


class BaseResponse(BaseModel):
    id: int
