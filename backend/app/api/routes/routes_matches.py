from fastapi import APIRouter, Depends
from app.services.api_football import get_fixtures
from app.services.api_brasileiro import get_brasil_fixtures
from app.services.probability_engine import identify_value_bets
from app.utils.cache import get_cached_data

router = APIRouter()

@router.get("/daily")
async def daily_matches():
    key = "daily_matches"
    data = await get_cached_data(key)
    if not data:
        fixtures = get_fixtures(date="today") + get_brasil_fixtures()
        value_bets = identify_value_bets(fixtures)
        data = {"fixtures": fixtures, "value_bets": value_bets}
        await get_cached_data(key, data, ttl=3600)
    return data