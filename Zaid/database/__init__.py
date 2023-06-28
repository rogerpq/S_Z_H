import redis
from config import REDIS_URL

redis_client = redis.StrictRedis.from_url(REDIS_URL)

# لحصول على قيمه
value = redis_client.get('key_name')

# لتعيين قيمة
redis_client.set('key_name', 'value')

# لحذف قيمة:
redis_client.delete('key_name')

dbb = redis.StrictRedis.from_url(REDIS_URL)
