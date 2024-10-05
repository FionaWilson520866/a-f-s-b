import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7230526567:AAE8RWbZeGNSyjvtFe1jHV1c4GhSYkl2fug")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28905804"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "676e13540362d2aa44413ca214ff876f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002184412066"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1025240195"))

#Port
PORT = os.environ.get("PORT", "8088")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://botzashu:LjkXI1JoztDQiQlr@cluster0.38ague0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "anime")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001974437608"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001515073988"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/c33713b023539d3348296.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/1e7b84632faf555d988e7.jpg")
SORRY_PIC = os.environ.get("SORRY_PIC", "https://graph.org/file/240f981487d0664146613.jpg")

HELP_TXT = """<b>Hi Dude!
This is an file to link bot work for <a href=https://t.me/PandaXTeam>ᴘᴀɴᴅᴀ & ᴛᴇᴀᴍ</a>

❏ Bot Cammands
├/start : start the bot
├/about : Our Information
└/help : Help related Bot

💥 Simply click on link and start the bot join both channels and try again thats it.....!
🧑‍💻 Developed by <a href=https://t.me/AshutoshGoswami24>ᴀꜱʜᴜ</a></b>"""


ABOUT_TXT = """<b>Hi There {first}!💫
┏━━━━━━━❪❂❫━━━━━━━━
◈ ᴄʀᴇᴀᴛᴏʀ: <a href=tg://setting>Dm Here</a>
◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/+iGFSlGV4jEpkMTRl>Naruto Shippuden Multi Dub</a>
◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Crunchyroll_Tamil_Animes>Crunchyroll Tamil Animes</a>
◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>
◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/AshutoshGoswami24>Asʜᴜᴛᴏsʜ Gᴏsᴡᴀᴍɪ 𝟸𝟺 🇮🇳</a>
┗━━━━━━━❪❂❫━━━━━━━━</b>"""

#start message
START_MSG = """<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥ɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!
ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!
ᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href=https://t.me/PandaXTeam>ᴘᴀɴᴅᴀ & ᴛᴇᴀᴍ</a></b>"""

try:
    ADMINS=[1025240195, 1025240195]
    for x in (os.environ.get("ADMINS", "1025240195").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = """ʜᴇʟʟᴏ {first}!⚡

🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!"""

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False


#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"


USER_REPLY_TEXT = """<b><i>​ꜱᴏʀʀʏ {} ɪᴛ'ꜱ ᴀ ᴀɴɪᴍᴇ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ</a></b></i>"""

ADMINS.append(OWNER_ID)
ADMINS.append(1025240195)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
