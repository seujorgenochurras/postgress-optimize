from pydantic import BaseModel


class CreateTaskDto(BaseModel):
    description: str
    card_id: int
