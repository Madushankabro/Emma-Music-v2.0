#JDampage <https://t.me/JDampage>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={})\n
ɪ ᴀᴍ ʟɪʟʏ ✘ ʀᴏʙᴏᴛ.  

[🙈](https://telegra.ph/file/0c0bfd5a1259718d5b6bd.jpg) ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ᴛʜᴇ ꜱᴏɴɢ ɴᴀᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ 📥\n ᴛʏᴘᴇ /ᴍᴜꜱɪᴄ"ꜱᴏɴɢ ɴᴀᴍᴇ" 🎵 \n ᴇɢ:```/music On My Way```

** 🎊 ᴀ ʙᴏᴛ ʙʏ : @EpicBotsSl**
** 👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ : @xMalitha**
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
                        "🔱 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🔱",  url= "https://t.me/LilyXRobot?startgroup=true"
                    )
                ],
                [
                     InlineKeyboardButton(
                        text="📣 ʙᴏᴛ ᴄʜᴀɴɴᴇʟ📣", url="https://t.me/epicbotssl"
                    ),
                    InlineKeyboardButton(
                        text="👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 👥", url="https://t.me/EpicChats"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        '🆘 ʜᴇʟᴘ 🆘', url = "https://t.me/xMalitha"
                    ),
                    InlineKeyboardButton(
                        '💾 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 💾', url = "https://github.com/xMalitha"
                    )
                 ],
                [
                    InlineKeyboardButton(
                        "ᴏᴛʜᴇʀ ʙᴏᴛs",  url= "https://t.me/EpicBotsSl/20"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ ʟɪʟʏ ✘ ʀᴏʙᴏᴛ ɪs ᴏɴʟɪɴᴇ")
idle()
