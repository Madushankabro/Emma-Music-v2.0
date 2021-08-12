#JDampage <https://t.me/JDampage>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), /nI'm very Powerful 💪 Sri Lankan 🇱🇰  🎶Song Downloader Bot 🎵

[😉](https://telegra.ph/file/d200133a770bb835fd7dc.jpg) Just send me the song name you want to download😋.Type /s"song name" 😊.There Is a an Example Below.
eg:```/s Faded```

A bot by @tgbotslkgroup
Maintance By @JDampage & @Zomething_else
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
                        text="Group🔥", url="https://t.me/tgbotslkgroup"
                    )
                    InlineKeyboardButton(
                        text="😊Add Me To A Group 😋", url="t.me/SLSongDL_Bot?startgroup=true"
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
