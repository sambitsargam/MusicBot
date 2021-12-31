from pyrogram import Client

from VoiceChat_Song_bot import config

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run
