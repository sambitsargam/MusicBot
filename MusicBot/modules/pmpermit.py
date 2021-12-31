from pyrogram import Client
import asyncio
from VoiceChat_Song_bot.config import SUDO_USERS
from VoiceChat_Song_bot.config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from VoiceChat_Song_bot.services.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "**Hi Dear , I am a Assistant of** [Aami](https://t.me/Aami_Song_bot) **for playing Music in Telegram Video Chats** .\n\n Sorry Bro or Sis Kindly Contact My Creator Now ☺️.\n [Creator](https://t.me/Telecat_X) \n\n If You Have any Complaints or Suggestions to Our Bot, Kindly Share With Creator or Share in @AAMIBOTSUPPORT ❤️\n Services Provided By @AAMIBOTUPDATES",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit turned off")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approved to PM due to outgoing messages. Don't send Spam Links or Personal Information about You😌")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", "/"]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM, Ask Your Doubts to [Creator](https://t.me/Telecat_X)")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", "/"]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()
