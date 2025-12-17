import httpx
from app.utils.cache import get_cached_data, set_cached_data

API_KEY = os.getenv("API_FUTEBOL_KEY")
BASE_URL = "https://api.api-futebol.com.br/v1/"

async def get_brasil_fixtures():
    key = "brasil_fixtures"
    data = await get_cached_data(key)
    if data:
        return data
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}live", headers={"Authorization": f"Bearer {API_KEY}"})
        data = resp.json()
        await set_cached_data(key, data, ttl=3600)
    return data

# Similar for standings /campeonatos/{id}/tabela, stats /partidas/{id}/estatisticas