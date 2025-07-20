
import redis

# Connect to Redis
cache = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def get_from_cache(key: str):
    return cache.get(key)

def set_to_cache(key: str, value: str, ex: int = 3600):
    cache.setex(key, ex, value)
