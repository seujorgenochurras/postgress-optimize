from pydantic import BaseModel


class CreateCardDto(BaseModel):
    user_id: int
    title: str
