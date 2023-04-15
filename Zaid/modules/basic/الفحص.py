import asyncio
from datetime import datetime
from platform import python_version

from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from config import ALIVE_PIC, ALIVE_TEXT
from Zaid import START_TIME
from Zaid import SUDO_USER
from Zaid.helper.PyroHelpers import ReplyCheck
from Zaid.modules.help import add_command_help
from Zaid.modules.bot.inline import get_readable_time

alive_logo = ALIVE_PIC or "https://telegra.ph//file/6ef37b30de52ad0a6f8ee.mp4"

if ALIVE_TEXT:
   txt = ALIVE_TEXT
else:
    txt = (
        f"** 𝐑𝐈𝐂𝐊𝐓𝐇𝐎𝐍 𝐈𝐒 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐍𝐎𝐖**\n\n"
        f"❏ **ꪜꫀ𝘳𝘴𝓲ꪮꪀ ‌♡⁩**: `1.0`\n"
        f"├• **ꪊρ𝓽𝓲ꪑꫀ 𝘳𝓲ᥴ𝘬𝓽ꫝꪮꪀ メ**: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"├• **ρꪗ𝓽ꫝꪮꪀ**: `{python_version()}`\n"
        f"├• **ρꪗ𝘳ꪮᧁ𝘳ꪖꪑ**: `{__version__}`\n"
        f"├• **مجموعة الدعم**: [Click](t.me/rickthon_group)\n"
        f"├• **𝘳𝓲ᥴ𝘬𝓽ꫝꪮꪀ ᥴꫝ **: [Click](t.me/rickthon)\n"
        f"└• **𝘿𝙀𝙑𝙎**: [اضغط هنا لرؤية المطورين](https://t.me/DevsRickthon/2)"        
    )

@Client.on_message(
    filters.command(["فحص", "ايقظ"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def alive(client: Client, message: Message):
    xx = await message.reply_text("✜| أهلًا بك عزيزي منصب ريك ثون انتظر قليلًا ")
    try:
       await message.delete()
    except:
       pass
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    xd = (f"{txt}")
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=xd,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(xd, disable_web_page_preview=True)

@Client.on_message(filters.command("ريك ثون", ".") & filters.me)
async def repo(bot: Client, message: Message):
    await message.edit("انتظر قليلًا")
    await asyncio.sleep(1)
    await message.edit("انتظر قليلًا لأريك قناة السورس.....")
    await asyncio.sleep(1)
    await message.edit("هذه هي قناة السورس: \n\n\nhttps://t.me/Rickthon\nالمطور : @PPF22 / @S_Z_H")


@Client.on_message(filters.command("المطور", ".") & filters.me)
async def creator(bot: Client, message: Message):
    await message.edit("**The best! \n @S_Z_H/@PPF22**")


@Client.on_message(filters.command(["مدة التشغيل", "up"], ".") & filters.me)
async def uptime(bot: Client, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await message.edit(f"Uptime ⚡\n" f"```{str(current_uptime).split('.')[0]}```")


@Client.on_message(filters.command("ايديي", ".") & filters.me)
async def get_id(bot: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**فايل ايدي**: `{rep.audio.file_id}`"
            file_id += "**نوع الفايل**: `audio`"

        elif rep.document:
            file_id = f"**ايدي الفايل**: `{rep.document.file_id}`"
            file_id += f"**نوع الفايل**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**ايدي الفايل**: `{rep.photo.file_id}`"
            file_id += "**نوع الفايل**: `photo`"

        elif rep.sticker:
            file_id = f"**ايدي الستيكر**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**ضع ستيكر**: `{rep.sticker.set_name}`\n"
                file_id += f"**ستيكر ايموجي**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker**: `False`\n"
            else:
                file_id += "**Sticker Set**: __None__\n"
                file_id += "**Sticker Emoji**: __None__"

        elif rep.video:
            file_id = f"**File ID**: `{rep.video.file_id}`\n"
            file_id += "**File Type**: `video`"

        elif rep.animation:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `GIF`"

        elif rep.voice:
            file_id = f"**File ID**: `{rep.voice.file_id}`\n"
            file_id += "**File Type**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.venue.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address**:\n"
            file_id += f"**title**: `{rep.venue.title}`\n"
            file_id += f"**detailed**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await message.edit(user_detail)

    else:
        await message.edit(f"**Chat ID**: `{message.chat.id}`")




add_command_help(
    "start",
    [
        [".فحص", "Check if the bot is alive or not."],
        [".ريك ثون", "Display the repo of this userbot."],
        [".الانشاء", "Show the creator of this userbot."],
        [".ايدي", "Send id of what you replied to."],
        [".مدة التشغيل `or` .uptime", "Check bot's current uptime."],
    ],
)

add_command_help(
    "restart",
    [
        [".restart", "You are retarded if you do not know what this does."],
    ],
)
