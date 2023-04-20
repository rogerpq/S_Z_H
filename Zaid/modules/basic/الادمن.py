import os
import sys
from re import sub
from time import time
import asyncio

from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message


DEVS = ["5582470474", "1260465030","1983379011","6101942278"]
admins_in_chat = {}

from Zaid.modules.help import add_command_help
from Zaid.modules.basic.profile import extract_user

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


async def list_admins(client: Client, chat_id: int):
    global admins_in_chat
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [
            member.user.id
            async for member in client.get_chat_members(
                chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
            )
        ],
    }
    return admins_in_chat[chat_id]["data"]




unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(
    filters.group & filters.command([" تعيين صوره الكروب","تعيين صوره المجموعة"], ".") & filters.me
)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("ليس لديك الصلاحيات الكافية لعمل الامر")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("سوي رد على الصوره ثم اكتب الامر")



@Client.on_message(filters.group & filters.command("حظر", ".") & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    rd = await message.edit_text("`جاري المعالجه`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("ليس لديك الصلاحيات الكافية لعمل الامر")
    if not user_id:
        return await rd.edit("لايمكنني العثور على هاذا الشخص")
    if user_id == client.me.id:
        return await rd.edit("تم الحظر بنجاح عزيزي")
    if user_id in DEVS:
        return await rd.edit("ماتكدر تحظر المطورين حبي")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("لا يمكنني حظر مشرف ، أنت تعرف القواعد ، وأنا كذلك.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    msg = (
        f"**اسم المستخدم المطرود :** {mention}\n"
        f"**تم طرده بواسطه :** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.ban_member(user_id)
    await rd.edit(msg)



@Client.on_message(filters.group & filters.command("الغاء الحظر", ".") & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    rd = await message.edit_text("`جاري المعالجه`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit(" لديك الصلاحيات الكافية لعمل الامر")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await rd.edit("لا يمكنك إلغاء حظر قناة")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await rd.edit(
            "رد على الشخص وسوي الامر او اكتب الامر وخلي يوزر الشخص"
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await rd.edit(f"تم الغاء حظر ! {umention}")



@Client.on_message(filters.command(["تثبيت", "الغاء التثبيت"], ".") & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await message.edit_text("رد على الرساله لتثبيتها او الغاء تثبيتها")
    rd = await message.edit_text("`جاري المعالجه`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await rd.edit(" لديك الصلاحيات الكافية لعمل الامر")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await rd.edit(
            f"**تم الغاء تثبيت الرساله : [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await rd.edit(
        f"**تم تثبيت الرساله : [this]({r.link}) message.**",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("كتم", ".") & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.edit_text("`جاري المعالجه ...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("ليس لديك الصلاحيات الكافية لعمل الامر")
    if not user_id:
        return await rd.edit("")
    if user_id == client.me.id:
        return await rd.edit("تم كتمه سيدي")
    if user_id in DEVS:
        return await rd.edit("نجب ماكدر اكتم المطورين مالتي")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("لا يمكنني كتم مشرف ، أنت تعرف القواعد ، وأنا كذلك.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**اسم المكتوم :** {mention}\n"
        f"**تم الكتم بواسطه :** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**السبب :** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await rd.edit(msg)



@Client.on_message(filters.group & filters.command("الغاء الكتم", ".") & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.edit_text("`جاري المعالجه`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("ليس لديك الصلاحيات الكافية لعمل الامر")
    if not user_id:
        return await rd.edit("لايمكنني العثور على هاذا الشخص")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await rd.edit(f"تم الغاء الكتم ! {umention}")


@Client.on_message(filters.command(["طرد", "بالنعال"], ".") & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.edit_text("`جار...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("ليس لدي صلاحيات!")
    if not user_id:
        return await rd.edit("لايمكنني الوصول الى الحساب.")
    if user_id == client.me.id:
        return await rd.edit("لايمكنك طرد نفسك.")
    if user_id == DEVS:
        return await rd.edit("لايمكنك طرد المطور انجب تريد تطرد المطور.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("لايمكنك طرد مشرف انت تعرف قواعد التلي.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**المطور:** {mention}
**تم الطرد من قبل:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**السبب:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await rd.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await rd.edit("**اسف انت مو ادمن**")


@Client.on_message(
    filters.group & filters.command(["رفع مشرف", "رفع ادمن"], ".") & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    rd = await message.edit_text("`جار...`")
    if not user_id:
        return await rd.edit("لايمكنني الوصول لحساب.")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await rd.edit("لا املك صلاحيات كاملة!")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await rd.edit(f"تم رفعه مشرف بنجاح! {umention}")

    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
        ),
    )
    await rd.edit(f"تم رفعه! {umention}")


@Client.on_message(filters.group & filters.command("تنزيل مشرف", ".") & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.edit_text("`جار...`")
    if not user_id:
        return await rd.edit("لايمكنني الوصول لحساب.")
    if user_id == client.me.id:
        return await rd.edit("لايمكنني انزال نفسي.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await rd.edit(f"تم تنزيله! {umention}")


add_command_help(
    "الادمن",
    [
        ["حظر [بالرد/بالمعرف/بالايدي]", "لحظر شخص."],
        [
            f"الغاء حظر [بالرد/بالمعرف/بالايدي]",
            "الغاء حظر شخص.",
        ],
        ["طرد [بالرد/بالمعرف/بالايدي]", "طرد شخص من كروب."],
        [
            f"رفع مشرف `او` .رفع ادمن",
            "لرفع شخص.",
        ],
        ["تنزيل مشرف", "لتنزيل شخص."],
        [
            "كتم [بالرد/بالمعرف/بالايدي]",
            "لكتم شخص.",
        ],
        [
            "الغاء الكتم [بالرد/بالمعرف/بالايدي]",
            "الغاء كتم شخص.",
        ],
        [
            "تثبيت [بالرد]",
            "لتثبيت رساله.",
        ],
        [
            "الغاء التثبيت [بالرد]",
            "لالغاء تثبيت رساله.",
        ],
        [
            "تعيين صوره المجموعة او تعيين صوره الكروب [بالرد على صورة]",
            "لتغير صورة الكروب",
        ],
    ],
)
