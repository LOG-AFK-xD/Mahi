import asyncio

from pytgcalls import idle
from driver.core import calls, bot, user

from config import (
    UBOT_ID,
    UBOT_NAME,
    UBOT_UNAME,
    BOT_ID,
    BOT_NAME,
    BOT_UNAME,
)


async def start_bot():
    await bot.start()
    BOT_ID = (await bot.get_me()).id
    BOT_NAME = (await bot.get_me()).first_name
    BOT_UNAME = (await bot.get_me()).username
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    
    await calls.start()
    UBOT_ID = (await user.get_me()).id
    UBOT_NAME = (await user.get_me()).first_name
    UBOT_UNAME = (await user.get_me()).username
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    
    await user.join_chat("levinachannel")
    await user.join_chat("veezsupportgroup")
    await idle()
    
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
