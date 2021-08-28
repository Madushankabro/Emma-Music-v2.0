#JDampage <https://t.me/JDampage>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm ✨ 𝐄𝐌𝐌𝐀 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 ✨.  

[😉](https://telegra.ph/file/d6a6f55cbf8a687163b0e.jpg) Just send me the song name you want to download😋.Type /music"song name" 😊.There Is a an Example Below.
eg:```/music bad habits```

**A bot by @epusthakalaya_bots**
**Developed By @kasu_bro 🇱🇰**
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
                        "🔱 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🔱",  url= "https://t.me/EmmaMusicPlayerBot?startgroup=true"
                    )
                ],
                [
                     InlineKeyboardButton(
                        text="📣 ʙᴏᴛ ᴄʜᴀɴɴᴇʟ📣", url="https://t.me/epusthakalaya_bots"
                    ),
                    InlineKeyboardButton(
                        text="👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 👥", url="https://t.me/epusthakalayabotsupport"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        '🆘 ʜᴇʟᴘ 🆘', url = "https://telegra.ph/%F0%9D%90%84%F0%9D%90%8C%F0%9D%90%8C%F0%9D%90%80-%F0%9D%90%8C%F0%9D%90%94%F0%9D%90%92%F0%9D%90%88%F0%9D%90%82-%F0%9D%90%81%F0%9D%90%8E%F0%9D%90%93-Help-08-27"
                    ),
                    InlineKeyboardButton(
                        '💾 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 💾', url = "https://github.com/TGBotsLk/SongBot"
                    )
                 ],
                [
                    InlineKeyboardButton(
                        "★ ʀᴇᴠɪᴇᴡ ᴜs ★ ",  url= "https://t.me/tlgrmcbot?start=emmamusicplayerbot"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ EMMA MUSIC BOT is online.")
idle()
