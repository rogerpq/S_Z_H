from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Zaid import SUDO_USER
from Zaid.modules.help import add_command_help

@Client.on_message(
    filters.command(["انضمام"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def join(client: Client, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`Processing...`")
    try:
        await client.join_chat(tex)
        await g.edit(f"**تم الانضمام بنجاح ايدي الشات** `{tex}`")
    except Exception as ex:
        await g.edit(f"**خطاء:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["مغادرة"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def leave(client: Client, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`جار...`")
    try:
        await xv.edit_text(f"{client.me.first_name} لقد غادر هذه المجموعة، إلى اللقاء!!")
        await client.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**الخطاء:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["مغادره كل المجموعات"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def kickmeall(client: Client, message: Message):
    tex = await message.reply_text("`جار المغادره في كل المجموعات...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**تم بنجاح المغادره في {done} المجموعات, خطاء في مغادره {er} المجموعات**"
    )


@Client.on_message(filters.command(["مغادره كل القنوات"], ".") & filters.me)
async def kickmeallch(client: Client, message: Message):
    ok = await message.reply_text("`جار المغادره في كل القنوات...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(
        f"**تم بنجاح المغادره في {done} القنوات, خطاء في مغادره {er} المجموعات**"
    )


add_command_help(
    "انضمام والمغادره",
    [
        [
            "اطردني",
            "للمغادرة!!.",
        ],
        ["مغادره كل المجموعات", "لمغادره كل المجموعات التي بحسابك."],
        ["مغادره كل القنوات", "لمغادره كل القنوات بحسابك."],
        ["انضمام + [يوزر القناة او مجموعة]", "لانضمام في مجموعة او قناة محدده."],
        ["مغادرة [يوزر القناة او المجموعة]", "لمغادرة في مجموعة او قناة محددة."],
    ],
)
