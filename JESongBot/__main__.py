#Uvindu Bro <https://t.me/UvinduBro>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER
await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Downloader Bot 🎵

A bot by @Uvindu_Bro 🇱🇰
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help ❓", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel 🔊", url="https://t.me/UvinduBr")
                                    ],[
                                      InlineKeyboardButton(
                                            "Source Code 📦", url="https://github.com/UvinduBro/UBSongBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>UB Songs Download Bot Help! 🎵

😉 Just send me the song name you want to download.😋

eg: ```/song Faded```


~ @UvinduBro</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back ⬅", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About ❕", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Source Code 📦", url="https://github.com/UvinduBro/UBSongBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About UB Songs Download Bot! 🎵</b>

<b>😉 Developer:</b> <a href="https://t.me/Uvindu_Bro">Uvindu Bro 🇱🇰</a>

<b>⁉ Support:</b> <a href="https://t.me/UvinduBr">Uvindu Bro</a>

<b>❤ Thanks:</b> <a href="https://t.me/Infinity_BOTs">Infinity BOTs</a>

<b>📚 Library:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>~ @UvinduBro</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back ⬅", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Source Code 📦", url="https://github.com/UvinduBro/UBSongBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

app.start()
LOGGER.info("✅ UBSongBot is online.")
idle()
