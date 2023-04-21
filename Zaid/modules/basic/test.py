from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import Message
from Zaid.modules.help import add_command_help


@Client.on_message(filters.command('تفسير','.') & filters.me)
async def chat_broadcast(c: Client, m: Message,online=False)
async def say(_, message: Message):
    if len(message.command) == 1:
        return
    command = " ".join(message.command[1:])
    await message.edit(f"<code>{command}</code>")


add_command_help(
    "تفسير",
    [
        ["تفسير", "أرسل رسالة لن يفسرها برنامج يوزربوت ."],
    ],
)