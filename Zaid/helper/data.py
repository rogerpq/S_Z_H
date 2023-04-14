from pyrogram.types import InlineKeyboardButton, WebAppInfo

class Data:

    text_help_menu = (
        "**قائمة الاوامر!**\n**— حط بدايه كل امر:** `.`"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
