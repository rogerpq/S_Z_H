from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from Zaid.database import cli as database
from Zaid.helper.PyroHelpers import ReplyCheck
#Dev file: @V_IRUuS
#Edit file : @newbaghdad
#دراكون_كان_هنا
@Client.on_message(filters.command("اكس او", ".") & filters.me)
async def xo(client: Client, message: Message):
	result = await client.get_inline_bot_results("xoBot", "play")
	await msg.delete()
	await client.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
	
	add_command_help(
"اكس او",
    [
[".اكس او", " بهاذا الامر ستلعب لعبه الاكس او الشهيره"],
    ],
)
