from pyrogram import filters, Client
from pyrogram.types import Message

from Zaid.modules.help import add_command_help

the_regex = r"^r\/([^\s\/])+"

f = filters.chat([])

if f:
   @Client.on_message(f)
   async def auto_read(bot: Client, message: Message):
       await bot.read_history(message.chat.id)
       message.continue_propagation()

#تخمط تثبت فشلك
@Client.on_message(filters.command("قرائة الرسائل تلقائي", ".") & filters.me)
async def add_to_auto_read(bot: Client, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("تم الغاء القرائة ")
    else:
        f.add(message.chat.id)
        await message.edit("تم تفعيل القرائة!")


add_command_help(
    "قرائة تلقائي",
    [
        [
            ".قرائة الرسائل تلقائي",
            "أرسل .قرائة الرسائل تلقائي في أي محادثة لقراءة جميع الرسائل المرسلة تلقائيًا حتى تتصل "
            " مرة أخرى .قرائة الرسائل تلقائي هذا مفيد إذا فتحت برنامج على شاشة أخرى.",
        ],
    ],
)
