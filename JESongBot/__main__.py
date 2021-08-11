#Uvindu Bro <https://t.me/UvinduBro>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm Song Downloader Bot 🎵

😉 Just send me the song name you want to download.😋
      eg:```/song Faded```
(https://telegra.ph/file/d200133a770bb835fd7dc.jpg)    
A bot by @tgbotslkchat
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Channel 🔊", url="https://t.me/tgbotslk"
                    ),
                    InlineKeyboardButton(
                        text="Dev 🔥", url="https://t.me/tgbotslkchat"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ SongBot is online.")
idle()
