from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 28962771))
API_HASH = getenv("API_HASH", "cec0e048dd9ca00d5c20020ada584278")
OWNER_ID = int(getenv("OWNER_ID", "7804637858"))
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "https://t.me/EvoKakarot")
UPDATE_CHNL = getenv("UPDATE_CHNL", "https://t.me/EvoKakarot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Not_Kakarot")

# Random Start Images
IMG = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]


# Random Stickers
STICKER = [
    "",
    "",
    "",
]


EMOJIOS = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
