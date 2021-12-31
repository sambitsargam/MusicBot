import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/c7c317caf779963c9c825.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "CatKing_ext")
OWNER_NAME = getenv("OWNER_NAME", "Telecat_X")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AAMIBOTSUPPORT")
PROJECT_NAME = getenv("PROJECT_NAME", "VoiceChat_Song_bot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Abhijith-Sudhakaran/VoiceChat_Song_bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "25"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
START_IMG = getenv("START_IMG","https://telegra.ph/file/fd294693240383d0a6af6.jpg")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1981831553").split()))
