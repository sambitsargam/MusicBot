
import logging
from time import time
from datetime import datetime
from VoiceChat_Song_bot.config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from VoiceChat_Song_bot.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VoiceChat_Song_bot.helpers.decorators import sudo_users_only

logging.basicConfig(level=logging.INFO)


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>[✨](https://telegra.ph/file/a488092b0f602ae43bbf0.jpg) **Welcome Dear♥️ {message.from_user.first_name}** \n
💭 **[{BOT_NAME}](https://t.me/Aami_song_bot) 𝗮𝗹𝗹𝗼𝘄 𝘆𝗼𝘂 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝗴𝗿𝗼𝘂𝗽𝘀 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗻𝗲𝘄 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺'𝘀 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁𝘀 !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url=f"https://t.me/{BOT_NAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(text="SEARCH HERE🔎", switch_inline_query_current_chat=""),
                    InlineKeyboardButton(text="GO INLINE🔎", switch_inline_query="")
                ],[
                    InlineKeyboardButton(
                        "⚙️ Initial Setup", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 Commands", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 Donate", url=f"https://t.me/Telecat_X") #these line can edit by your own Username!
                ],[
                    InlineKeyboardButton(
                        "👥 Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📣 Updates's", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "🧪 Source Code 🧪", url="https://github.com/Abhijit-Sudhakaran/VoiceChat_Song_bot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **All Services of {BOT_NAME} is Currently Alive!**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛔ Report", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📣 What's New!", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

⚡Powered by {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ HOW TO USE ME", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡Powered by {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging network speed...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🌐 `Network Ping!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`\n"
        f"**Server: Heroku**"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"🤖 {BOT_NAME} status:\n"
        f"• **Uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`\n"
        f"• **TimeZone:** [India](https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.timeanddate.com/time/zone/india&ved=2ahUKEwiEy5TSi7bzAhVbYysKHeD1D7MQFnoECCEQAQ&usg=AOvVaw0OdJTFodzNXxEP8saCiuDE)"
    )
