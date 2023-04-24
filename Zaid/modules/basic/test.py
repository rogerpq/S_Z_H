from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import Message
from Zaid.modules.help import add_command_help


@Client.on_message(filters.command("انتحال", ".") & filters.me)
async def clone(client: Client, message: Message):
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
