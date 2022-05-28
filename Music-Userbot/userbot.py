import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


#@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
#async def ping(client, m: Message):
#    await m.delete()
#    start = time()
#    current_time = datetime.utcnow()
#    m_reply = await m.reply_text("⚡")
#    delta_ping = time() - start
#    uptime_sec = (current_time - START_TIME).total_seconds()
#    uptime = await _human_time_duration(int(uptime_sec))
#    await m_reply.edit(
#        f"<b>🏓 PONG</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳ AKTIF</b> - `{uptime}`"
#    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("APE LU KONTOL")
    await loli.edit("TUNGGU BENTAR YA BANGSAT")
    await loli.edit("GUA CUMAN RESTART")
    await loli.edit("BENTARAN DOANG KOK")
    await loli.edit("KALAU GA SABAR")
    await loli.edit("MATI AJA GAPAPA")
    await loli.edit("ANEH BAT LU ")
    await loli.edit("DAH TOD GUA MAU RESTART DLU")
    await loli.edit("BYE")
    await loli.edit("**✅ Userbot Di Mulai Ulang**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Hallo {m.from_user.mention}!

🛠 MENU BANTUAN

⚡ PERINTAH UNTUK SEMUA ORANG
• {HNDLR}vplay [judul video | link youtube | balas file video] - untuk memutar video
• {HNDLR}playlist untuk melihat daftar putar
• {HNDLR}help - untuk melihat daftar perintah

⚡ PERINTAH UNTUK SEMUA ADMIN
• {HNDLR}vresume - untuk melanjutkan pemutaran Video
• {HNDLR}vpause - untuk untuk menjeda pemutaran Video
• {HNDLR}vskip - untuk melewati lagu atau Video
• {HNDLR}vend - untuk mengakhiri pemutaran</b>
"""
    await m.reply(HELP)



