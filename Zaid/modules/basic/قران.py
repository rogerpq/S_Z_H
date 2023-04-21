from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import * 
from pyrogram.types import *
import asyncio
from requests import get
from random import * 
from datetime import datetime




#حتى تريد تخمط امر قران بعد الله شيسوي بيك
#DEV SAIF

@Client.on_message(filters.command('قرأن','.') & filters.me)
async def chat_broadcast(c: Client, m: Message,online=False):
 online = True
 while online:
  res = get(f"http://api.alquran.cloud/v1/ayah/{str(randint(1,6236))}/ar.abdulsamad").json()
  x = {
   "text":res['data']['text'] ,
   "mp3":res['data']['audio'] ,
   "name":res['data']['surah']['name'] , 
   "part":res['data']['juz'] , 
   "page":res['data']['page'] , 
   "hizb":res['data']['hizbQuarter'] , 
   "ayh":res['data']['numberInSurah'],}
  text = f"""• {x['name']} • \n\n*﴿ {x['text']} ﴾* \n\n- الجزء: {x['part']} - الحزب: {x['hizb']} - الأية: {x['ayh']} - الصفحة: {x['page']} . \n\n"""
  async for dialog in c.get_dialogs():
   if dialog.chat.type == enums.ChatType.PRIVATE:
    try:
     await c.send_audio(dialog.chat.id,x['mp3'],
     text)
    except Exception as e:
     await m.reply(e)
  await asyncio.sleep(86400)


