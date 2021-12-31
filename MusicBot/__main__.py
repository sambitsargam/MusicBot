import requests
from pyrogram import Client as Bot

from VoiceChat_Song_bot.config import API_HASH
from VoiceChat_Song_bot.config import API_ID
from VoiceChat_Song_bot.config import BG_IMAGE
from VoiceChat_Song_bot.config import BOT_TOKEN
from VoiceChat_Song_bot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./PicsArt_10-02-05.45.42.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MusicBot.modules"),
)

bot.start()
run()
