from fastapi import APIRouter
from pydantic import BaseModel

class ChatInput(BaseModel):
    message: str

router = APIRouter()

@router.post("/")
async def chat(input: ChatInput):
    # Simple parsing
    if "jogos de hoje" in input.message.lower():
        return get_fixtures(date="today")
    elif "value bets" in input.message.lower():
        return identify_value_bets(get_fixtures())
    elif "over 2.5" in input.message.lower():
        return filter_over_bets(get_odds())
    return {"response": "Comando não entendido."}
# Prepared for Telegram: Can expose webhook later