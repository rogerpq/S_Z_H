from pyrogram import Client, filters
from pyrogram.types import Message

from Zaid.modules.help import add_command_help


@Client.on_message(filters.command("انشاء", ".") & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.edit_text(
            message, f"**اكتب .help create إذا كنت بحاجة إلى مساعدة**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.edit_text("`جار...`")
    desc = "Welcome To My " + ("كروب" if group_type == "كروب" else "قناة")
    if group_type == "كروب":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await xd.edit(
            f"**تم انشاء المجموعة بنجاح : [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "قناة":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await xd.edit(
            f"**تم انشاء القناة ينجاح : [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "create",
    [
        ["create ch", "create an channel"],
        ["create gc", "create an group"],
    ],
)
