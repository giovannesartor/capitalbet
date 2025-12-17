from fastapi import APIRouter
from app.services.odds_comparator import compare_odds
from app.services.api_football import get_odds

router = APIRouter()

@router.get("/compare/{fixture_id}")
async def compare(fixture_id: int):
    odds = get_odds(fixture_id)
    compared = compare_odds(odds)  # Best odds per market
    return compared