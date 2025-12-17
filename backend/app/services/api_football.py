import httpx
from app.utils.cache import get_cached_data, set_cached_data

API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io/"

async def get_fixtures(date=None):
    key = f"fixtures_{date or 'today'}"
    data = await get_cached_data(key)
    if data:
        return data
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}fixtures", params={"date": date}, headers={"x-apisports-key": API_KEY})
        data = resp.json()["response"]
        await set_cached_data(key, data, ttl=3600)
    return data

# Similar for get_odds(fixture_id), get_statistics(fixture_id), get_h2h(team1, team2), get_standings(league, season)

def fetch_daily_fixtures():  # For background
    get_fixtures()