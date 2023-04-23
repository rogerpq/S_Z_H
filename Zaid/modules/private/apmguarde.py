from pyrogram import filters, Client
import asyncio
from Zaid import SUDO_USER
from Zaid.modules.help import *
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users

import Zaid.database.pmpermitdb as Zaid



@Client.on_message(filters.command("حماية الخاص", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**انا يمكنني فهم فقط التفعيل او الايقاف!**")
        return
    if arg == "ايقاف":
        await Zaid.set_pm(False)
        await message.edit("**تم ايقاف حماية الخاص بنجاح**")
    if arg == "تفعيل":
        await Zaid.set_pm(True)
        await message.edit("**تم تشغيل حماية الخاص بنجاح**")
@Client.on_message(filters.command("ضع رسالة التحذير", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**ماهي الرساله التي يجب تعيينها؟**")
        return
    if arg == "الرسالة العادية":
        await Zaid.set_permit_message(Zaid.PMPERMIT_MESSAGE)
        await message.edit("**تم ارجاع رساله التحذير العادية**.")
        return
    await Zaid.set_permit_message(f"`{arg}`")
    await message.edit("**تم وضع رساله التحذير الخاصه بك بنجاح!**")


add_command_help(
    "حماية الخاص",
    [
        [".حماية الخاص [تفعيل او ايقاف]", " -> لتشغيل حماية الخاص او اطفاء حماية الخاص."],
        [".ضع رسالة التحذير [الرسالة او الرسالة العادية]", " -> لوضع رسالة ترحيب خاصة بك."],
        [".ضع رسالة الحظر [الرسالة او الرسالة العادية]", "-> لوضع رسالة حظر خاصة بك."],
        [".setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [".allow", " -> Allows a user to PM you."],
        [".deny", " -> Denies a user to PM you."],
    ],
)
