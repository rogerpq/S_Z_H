from asyncio import gather
from os import remove

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from Zaid.helper.PyroHelpers import ReplyCheck
from Zaid.modules.basic.profile import extract_user

from Zaid.modules.help import add_command_help

#RICKTHON SOURCE

@Client.on_message(filters.command(["كشف", "معلوماتة"], ".") & filters.me)
async def who_is(client: Client, message: Message):
    user_id = await extract_user(message)
    ex = await message.edit_text("`جار . . .`")
    if not user_id:
        return await ex.edit(
            "**يرجى كتابه الامر مع ايدي المستخدم/معرف المستخدم/الرد على مستخدم ليتم جلب معلوماته.**"
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""<b>معلومات المستخدم:</b>

🆔 <b>معرف المستخدم:</b> <code>{user.id}</code>
👤 <b>اسم المستخدم:</b> {first_name}
🗣️ <b>اسم الثاني:</b> {last_name}
🌐 <b>المعرف:</b> {username}
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🤖 <b>هل المستخدم بوت:</b> <code>{user.is_bot}</code>
🚷 <b>هل هو احتيالي:</b> <code>{user.is_scam}</code>
🚫 <b>هل هو مقيد:</b> <code>{user.is_restricted}</code>
✅ <b>هل هو موثق:</b> <code>{user.is_verified}</code>
⭐ <b>بريميوم:</b> <code>{user.is_premium}</code>
📝 <b>بايو المستخدم:</b> {bio}

👀 <b>المجموعات المشتركة:</b> {len(common)}
👁️ <b>اخر ظهور:</b> <code>{status}</code>
🔗 <b>رابط الحساب:</b> <a href='tg://user?id={user.id}'>{fullname}</a>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                ex.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await ex.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await ex.edit(f"**المعلومات:** `{e}`")


@Client.on_message(filters.command(["معلومات الدردشة", "كشف المجموعة", "ginfo"], ".") & filters.me)
async def chatinfo_handler(client: Client, message: Message):
    ex = await message.edit_text("`جار...`")
    try:
        if len(message.command) > 1:
            chat_u = message.command[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await message.edit(
                    f"**• استخدم هذا الامر في المجموعة او اكتبه مع معرف المجموعة/ايدي المجموعة**"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""<b>معلومات المجموعة:</b>

🆔 <b>ايدي المجموعة:</b> <code>{chat.id}</code>
👥 <b>الاسم:</b> {chat.title}
👥 <b>المعرف:</b> {username}
📩 <b>نوع:</b> <code>{type}</code>
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🗣️ <b>احتيالي:</b> <code>{chat.is_scam}</code>
🎭 <b>مزيف:</b> <code>{chat.is_fake}</code>
✅ <b>موثق:</b> <code>{chat.is_verified}</code>
🚫 <b>مقيد:</b> <code>{chat.is_restricted}</code>
🔰 <b>محمي:</b> <code>{chat.has_protected_content}</code>

🚻 <b>الاعضاء:</b> <code>{chat.members_count}</code>
📝 <b>البايو:</b>
<code>{description}</code>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                ex.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await ex.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await ex.edit(f"**المعلومات:** `{e}`")


add_command_help(
    "كشف",
    [
        [
            "كشف <username/userid/reply>",
            "جلب معلومات مستخدم تليجرام.",
        ],
        [
            "معلومات الدردشة <username/chatid/reply>",
            "جلب جميع معلومات الدردشة.",
        ],
    ],
)
