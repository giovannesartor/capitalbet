from fastapi import APIRouter
from app.services.api_football import get_statistics, get_h2h, get_standings
from app.services.api_brasileiro import get_brasil_stats

router = APIRouter()

@router.get("/{fixture_id}")
async def stats(fixture_id: int):
    stats = get_statistics(fixture_id)
    h2h = get_h2h(fixture_id)  # Need teams from fixture
    standings = get_standings()  # League
    brasil_stats = get_brasil_stats(fixture_id) if is_brasil else {}
    return {"stats": stats, "h2h": h2h, "standings": standings, "brasil": brasil_stats}