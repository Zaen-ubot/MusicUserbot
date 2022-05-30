import asyncio

from pytgcalls import idle
from Music-Userbot import arq
from config import call_py

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
