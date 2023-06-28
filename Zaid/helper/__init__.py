import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zaid"])

async def join(client):
    try:
        await client.join_chat("rickthon")
        await client.join_chat("rickthon_support")
        await client.join_chat("x7_cm")
    except BaseException:
        pass
