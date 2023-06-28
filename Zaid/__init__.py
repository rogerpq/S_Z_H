from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

if API_ID:
   API_ID = API_ID
else:
   print("Warning Im Useing The Random Api Id⚡")
   API_ID = "6435225"

if API_HASH:
   API_HASH = API_HASH
else:
   print("Warning Im Useing The Random Api Hash ⚡")   
   API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
   print("تحذير : لم يتم العثور على توكن يرجى اضافه التوكن⚡")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

if STRING_SESSION:
   print("Client1: تم العثور علية.. جار البدء..📳")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="Zaid/modules"))
   clients.append(client1)
