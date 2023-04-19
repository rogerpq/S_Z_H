import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType, UserStatus
from pyrogram.types import Message
from Zaid import SUDO_USER
from pyrogram.errors.exceptions.flood_420 import FloodWait

from Zaid.modules.help import add_command_help


@Client.on_message(
    filters.command(["ضيف"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def inviteee(client: Client, message: Message):
    mg = await message.reply_text("`Adding Users!`")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("`أعطني مستخدمين لإضافتهم! تحقق من قائمة التعليمات لمزيد من المعلومات!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`غير قادر على إضافة المستخدمين! \nTraceBack : {e}`")
        return
    await mg.edit(f"`تم الإضافة {len(user_list)} إلى هذه المجموعة / القناة!`")

@Client.on_message(
    filters.command(["دعوة الكل"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def inv(client: Client, message: Message):
    ex = await message.reply_text("`جاري المعالجة . . .`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await ex.edit_text(f"دعوة المستخدمين من {chat.username}")
    async for member in client.get_chat_members(chat.id):
        user = member.user
        zxb = [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]
        if user.status in zxb:
            try:
                await client.add_chat_members(tgchat.id, user.id)
            except FloodWait as e:
                return
            except Exception as e:
                pass

@Client.on_message(filters.command("الرابط", ".") & filters.me)
async def invite_link(client: Client, message: Message):
    um = await message.edit_text("`جاري المعالجة...`")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        message.chat.title
        try:
            link = await client.export_chat_invite_link(message.chat.id)
            await um.edit(f"**رابط الدعوة:** {link}")
        except Exception:
            await um.edit("Denied permission")


add_command_help(
    "invite",
    [
        [
            "رابط الدعوة",
            "إعطاء رابط الدعوة الخاص بالمجموعة. [تحتاج مشرف]",
        ],
        ["دعوة @username", "لإضافة بعض الأشخاص."],
        ["دعوة الكل @username", "الجمع الشامل (يمكن أن تؤثر على حسابك)."],
    ],
)
