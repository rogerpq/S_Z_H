from Zaid import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "✘ أهلًا بك عزيزي 👋!\n\n✘ أنا المساعد الخاص بك?\n\n‣ أنا أستطيع مساعدتك في معرفة أوامر السورس.\n\n‣ المطور: @S_Z_H \n\n‣ شكرًا لك لتنصيب ريك ثون\n\n‣ ارسل /clone {لارسال كود بايروجرام الخاص بك}"
)

@app.on_message(filters.user(OWNER_ID) & filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("𝗗𝗘𝗩 𝗥𝗜𝗖𝗞𝗧𝗛𝗢𝗡", url="t.me/S_Z_H"),
            ],
            [
                InlineKeyboardButton("𝗗𝗘𝗩 𝗥𝗜𝗖𝗞𝗧𝗛𝗢𝗡", url="t.me/S_Z_H"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("تمهيد العميل الخاص بك")
                   # change thiDirectry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"لقد نجح عميلك كـ {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**حدث خطأ ما:** `{str(e)}`\n اضغط /start مرة أخرى.")
#تعريب - @PPF22 # تعريبه كله غلط ونص التعريب حاط حقوقه
# روجر كان هنا - @E_7_V
