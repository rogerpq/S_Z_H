from pyrogram import Client, filters
import pytz
from pytz import timezone, all_timezones
from Zaid.modules.help import add_command_help
import asyncio
from Zaid import SUDO_USER

#KiNg SAIF

#تخمط وماتذكر حقوق اختك انكحها

# Set the delay between name updates (in seconds). 
DELAY_TIME = 60 
 
# Define the available fonts to use for time display. 
NORMAL_TEXT = "0123456789: " 
NAME_FONT = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗: " 
 
# List to store the state of the time name update. 
time_name = [] 
 
@Client.on_message(filters.me & filters.command('اسم وقتي', '.')) 
async def time_name_cmd(client, message): 
    # Clear the list and add "on" to indicate the time name update is on. 
    time_name.clear() 
    time_name.append("on") 
    await message.edit("تم تفعيل اسم الوقتي بنجاح✅") 
 
    while True: 
        if time_name[0] == "off": 
            break 
        else: 
            iraq_time_zone = pytz.timezone('Asia/Baghdad') 
            current_time = datetime.now(iraq_time_zone).strftime("%I:%M") 
            name = await convert_numbers_to_name_font(current_time, NORMAL_TEXT, NAME_FONT) 
            print(name) 
            try: 
                await client.update_profile(last_name=name) 
            except FloodWait as ex: 
                print(str(ex)) 
                await asyncio.sleep(ex.seconds) 
            await asyncio.sleep(DELAY_TIME) 
 
async def convert_numbers_to_name_font(text, normal_text, name_font): 
    """ 
    Convert the numbers in the text to the corresponding unicode name fonts. 
    """ 
    result = "" 
    for char in text: 
        if char in normal_text: 
            result += name_font[normal_text.index(char)] 
        else: 
            result += char 
    return result 
 
 
@Client.on_message(filters.me & filters.command('ايقاف اسم وقتي', '.')) 
async def stop_time_name_cmd(client, message): 
    # Clear the list and add "off" to indicate the time name update is off. 
    time_name.clear() 
    time_name.append("off") 
    await message.edit("تم ايقاف اسم الوقتي بنجاح ✔️")


add_command_help(
    "اسم وقتي",
    [
        ["اسم وقتي", "لتفعيل اسم الوقتي."],
        [
            "ايقاف اسم وقتي",
            "لايقاف اسم الوقتي.",
        ],
    ],
)
