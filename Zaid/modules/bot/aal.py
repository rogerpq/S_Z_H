from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from pyrogram import Client

 

ALIVE_PIC = 'https://graph.org//file/6ef37b30de52ad0a6f8ee.mp4'
@Client.on_message(filters.command(["awake", "alive"], [".", "!"]))
async def allive(client: Client, e: Message):
    try:
        me = await client.get_me()
        Alive_msg = f"𝐑𝐈𝐂𝐊𝐓𝐇𝐎𝐍 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ ID : `{me.id}` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/rickthon_group) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
            photo=ALIVE_PIC,
            caption=Alive_msg,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/RICKTHON")
                ], [
                    InlineKeyboardButton(
                        "• 𝐃𝐄𝐕 •", url="https://t.me/S_Z_H")
                ]],
            ),
        ) 
    except Exception as lol:         
        Alive_msg = f"𝐑𝐈𝐂𝐊𝐓𝐇𝐎𝐍 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ](https://t.me/rickthon_group) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
            photo=ALIVE_PIC,
            caption=Alive_msg,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/RICKTHON"),
                    ],
                    [
                        InlineKeyboardButton("• 𝐃𝐄𝐕 •", url="https://t.me/S_Z_H"),
                    ],
                ],
            ),
        )
