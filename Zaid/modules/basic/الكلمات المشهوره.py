#مخصص لريكثون
import time
#kiNg Dragon
#KinG @Rickthon
from pyrogram import filters, Client
from pyrogram.types import Message

from Zaid.modules.help import add_command_help


class Custom(dict):
    def __missing__(self, key):
        return 0


@Client.on_message(filters.command("الكلمات المشهوره", ".") & filters.me)
async def word_count(bot: Client, message: Message):
    await message.delete()
    words = Custom()
    progress = await bot.send_message(message.chat.id, "`معالجة 0 رسائل`")
    total = 0
    async for msg in bot.iter_history(message.chat.id, 10000):
        total += 1
        if total % 100 == 0:
            await progress.edit_text(f"`تمت معالجة {total} من الرسائل`")
            time.sleep(0.5)
        if msg.text:
            for word in msg.text.split():
                words[word.lower()] += 1
        if msg.caption:
            for word in msg.caption.split():
                words[word.lower()] += 1
    freq = sorted(words, key=words.get, reverse=True)
    out = "عداد الكلمات\n"
    for i in range(30):
        out += f"{i + 1}. **{words[freq[i]]}**: {freq[i]}\n"

    await progress.edit_text(out)


add_command_help(
    "الكلمات المشهوره",
    [
        [
            ".الكلمات المشهوره",
            "اهلا عزيزي , اهميه الامر يضهر لك 30 كلمه مشهوره من بين عشره الاف رساله !"
            "والدردشه الذي تريد العثور على الكلمات المشهوره فيها",
        ],
    ],
)
