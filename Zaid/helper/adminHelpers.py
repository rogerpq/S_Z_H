import asyncio
from time import time

from pyrogram.types import Message

from pyrogram import Client 
from Zaid.helper.interval import IntervalHelper


async def CheckAdmin(message: Message):
    """التحقق اذا كنت انا ادمن ام لا."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await Client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__انا لست ادمن!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__ما عندك صلاحية لتقييد الاعضاء عزيزي__")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """تحقق مما إذا كانت الرسالة ردا على مستخدم آخر."""
    if not message.reply_to_message:
        await message.edit("يجب عليك الرد على مستخدم")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"لايمكنني {message.command[0]} نفسي.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"لايمكنني {message.command} هذا المستخدم.")
    await asyncio.sleep(2)
    await message.delete()
