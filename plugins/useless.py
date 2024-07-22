from bot import Bot
from pyrogram.types import *
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT, SORRY_PIC
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


#@Bot.on_message(filters.private & filters.incoming)
#async def useless(_,message: Message):
#    if USER_REPLY_TEXT:
#        await message.reply(USER_REPLY_TEXT)

@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):            
    user = message.from_user  # Retrieve the user who sent the message
    button = InlineKeyboardMarkup([[
            InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", url='https://t.me/PandaXTeam')
        ]])
    if SORRY_PIC:
        await message.reply_photo(SORRY_PIC, caption=USER_REPLY_TEXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=USER_REPLY_TEXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)


