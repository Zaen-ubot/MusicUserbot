import asyncio

from pytgcalls import idle

from config import call_py
from Music-Userbot.quote import arq


async def main():
    await call_py.start()
    print(
        """
    --------------------------
   |   Music-Userbot Actived  |
    --------------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
