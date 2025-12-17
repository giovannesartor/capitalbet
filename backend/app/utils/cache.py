import os
import redis
import json

r = redis.from_url(os.getenv("REDIS_URL"))

async def get_cached_data(key):
    data = r.get(key)
    return json.loads(data) if data else None

async def set_cached_data(key, data, ttl):
    r.set(key, json.dumps(data), ex=ttl)