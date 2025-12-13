# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "20288395"))
API_HASH = getenv("API_HASH", "1245317c7706166809189b4a7918b79c")
BOT_TOKEN = getenv("BOT_TOKEN", "8538134836:AAEuDJEfchE-QNslpGeMD7avohn7V8ZtxQs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8429266518").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://jeetendra2949_db_user:4FE5y1WlDhZSGV1Y@cluster0.glaqca4.mongodb.net/?appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003320690267")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003357360615"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
