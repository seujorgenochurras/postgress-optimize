from fastapi import APIRouter
from prisma.partials import CardWithoutRelation
from src.dto.CreateCardDto import CreateCardDto
from src.injector import Resolve
from src.service.CardService import CardService

router = APIRouter(prefix="/card", tags=["card"])

card_service = Resolve(CardService)

@router.post("/", response_model=CardWithoutRelation) 
async def create_card(create_card_dto: CreateCardDto):
    return await card_service().create(create_card_dto.user_id, create_card_dto.title)
