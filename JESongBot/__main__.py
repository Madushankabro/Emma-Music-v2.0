#JDampage <https://t.me/JDampage>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm โจ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐ โจ.  

[๐](https://telegra.ph/file/d6a6f55cbf8a687163b0e.jpg) Just send me the song name you want to download๐.Type /music"song name" ๐.There Is a an Example Below.
eg:```/music bad habits```

**A bot by @epusthakalaya_bots**
**Developed By @kasu_bro ๐ฑ๐ฐ**
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
                        "๐ฑ แดแดแด แดแด แดแด สแดแดส ษขสแดแดแด ๐ฑ",  url= "https://t.me/EmmaMusicPlayerBot?startgroup=true"
                    )
                ],
                [
                     InlineKeyboardButton(
                        text="๐ฃ สแดแด แดสแดษดษดแดส๐ฃ", url="https://t.me/epusthakalaya_bots"
                    ),
                    InlineKeyboardButton(
                        text="๐ฅ sแดแดแดแดสแด ษขสแดแดแด ๐ฅ", url="https://t.me/epusthakalayabotsupport"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        '๐ สแดสแด ๐', url = "https://telegra.ph/%F0%9D%90%84%F0%9D%90%8C%F0%9D%90%8C%F0%9D%90%80-%F0%9D%90%8C%F0%9D%90%94%F0%9D%90%92%F0%9D%90%88%F0%9D%90%82-%F0%9D%90%81%F0%9D%90%8E%F0%9D%90%93-Help-08-27"
                    ),
                    InlineKeyboardButton(
                        '๐พ sแดแดสแดแด แดแดแดแด ๐พ', url = "https://github.com/Madushankabro/Emma-Music-v2.0"
                    )
                 ],
                [
                    InlineKeyboardButton(
                        "โ สแดแด?ษชแดแดก แดs โ ",  url= "https://t.me/tlgrmcbot?start=emmamusicplayerbot"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("โ EMMA MUSIC BOT is online.")
idle()
