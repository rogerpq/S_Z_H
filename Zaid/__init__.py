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
   print("تحذير : لم يتم العثور على الايبي ايدي ساستخدم ايبي ايدي سيف⚡")
   API_ID = "6435225"

if API_HASH:
   API_HASH = API_HASH
else:
   print("تحذير : لم يتم العثور على ايبي هاش ساستخدم ايبي هاش سيف⚡")   
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

if STRING_SESSION1:
   print("Client1: تم العثور علية.. جار البدء..📳")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="Zaid/modules"))
   clients.append(client1)

if STRING_SESSION2:
   print("Client2: تم العثور علية..جار البدء.. 📳")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="Zaid/modules"))
   clients.append(client2)

if STRING_SESSION3:
   print("Client3: تم العثور عليه..جار البدء.. 📳")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="Zaid/modules"))
   clients.append(client3)

if STRING_SESSION4:
   print("Client4: تم العثور عليه..جار البدء.. 📳")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="Zaid/modules"))
   clients.append(client4)

if STRING_SESSION5:
   print("Client5: تم العثور علية..جار البدء.. 📳")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="Zaid/modules"))
   clients.append(client5)

if STRING_SESSION6:
   print("Client6: تم العثور علية..جار البدء.. 📳")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="Zaid/modules"))
   clients.append(client6)

if STRING_SESSION7:
   print("Client7: تم العثور علية..جار البدء.. 📳")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="Zaid/modules"))
   clients.append(client7)

if STRING_SESSION8:
   print("Client8: تم العثور علية..جار البدء.. 📳")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="Zaid/modules"))
   clients.append(client8)

if STRING_SESSION9:
   print("Client9: تم العثور علية..جار البدء.. 📳")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="Zaid/modules"))
   clients.append(client9)

if STRING_SESSION10:
   print("Client10: تم العثور علية..جار البدء.. 📳")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="Zaid/modules")) 
   clients.append(client10)
