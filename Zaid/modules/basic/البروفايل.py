import os
from asyncio import sleep
import os
import sys
from re import sub
from time import time


from pyrogram import Client, filters, enums
from pyrogram.types import Message

from Zaid import SUDO_USER
from Zaid.helper.PyroHelpers import ReplyCheck

from Zaid.modules.help import add_command_help

flood = {}
profile_photo = "cache/pfp.jpg"


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]

@Client.on_message(
    filters.command(["الغاء البلوك"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`انتظر قليلًا جاي الغاء البلوك عنه . . .`")
    if not user_id:
        return await message.edit(
            "يجب عليك الرد على المستخدم او الغاء البلوك + يوزره أو ايديه."
        )
    if user_id == client.me.id:
        return await tex.edit("تم إلغاء البلوك عنه.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**تم إلغاء الحظر عن** {umention}")

@Client.on_message(
    filters.command(["بلوك"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`جاري حظره . . .`")
    if not user_id:
        return await tex.edit_text(
            "Provide User ID/Username or reply to user message to block."
        )
    if user_id == client.me.id:
        return await tex.edit_text("تم حظره ✅.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**Successfully blocked** {umention}")


@Client.on_message(
    filters.command(["وضع اسم"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def setname(client: Client, message: Message):
    tex = await message.reply_text("`جاري وضع اسم . . .`")
    if len(message.command) == 1:
        return await tex.edit(
            "عذرًا عزيزي عليك كتابة الأسم أولًا"
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(f"**تم تغيير الأسم الخاص بك إلى** `{name}`")
        except Exception as e:
            await tex.edit(f"**خطأ:** `{e}`")
    else:
        return await tex.edit(
            "أدخل نصًا لتعيينه كاسمك."
        )

@Client.on_message(
    filters.command(["وضع بايو"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def set_bio(client: Client, message: Message):
    tex = await message.edit_text("`جاري وضع بايو . . .`")
    if len(message.command) == 1:
        return await tex.edit("Provide text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"**تم تغيير البايو الخاص بك إلى.** `{bio}`")
        except Exception as e:
            await tex.edit(f"**خطأ:** `{e}`")
    else:
        return await tex.edit("يجب عليك كتابة النص لتعيينه البايو.")


@Client.on_message(
    filters.command(["وضع صورة"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("**تم تغيير الصورة الخاص بك.**")
    else:
        await message.reply_text(
            "يجب عليك الرد على الصورة لتعيينها لحسابك"
        )
        await sleep(3)
        await message.delete()


@Client.on_message(
    filters.command(["وضع فيديو"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.reply_text("لم يتم العثور على صورة الملف الشخصي!")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)


add_command_help(
    "profile",
    [
        ["block", "to block someone on telegram"],
        ["unblock", "to unblock someone on telegram"],
        ["setname", "set your profile name."],
        ["setbio", "set an bio."],
        [
            "setpfp",
            f"reply with image to set your profile pic.",
        ],
        ["vpfp", "Reply with video to set your video profile."],
    ],
)
