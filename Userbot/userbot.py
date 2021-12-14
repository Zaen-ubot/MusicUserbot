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


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("🥵")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🙈 Ciluk</b> `{delta_ping * 1000:.3f} ms` \n<b>🙉 Baaa</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Asisten Rafen memulai restart.**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Hallo {m.from_user.mention}!

🛠 MENU BANTUAN Asisten Rafen 

⚡ PERINTAH UNTUK SEMUA ORANG KECUALI ORANG MENINGGAL
• {HNDLR}Play🎵 [judul lagu | link youtube | balas file audio] - untuk memutar lagu
• {HNDLR}Videoplay📺 [judul video | link youtube | balas file video] - untuk memutar video
• {HNDLR}Playlist🔖 untuk melihat daftar putar
• {HNDLR}Ping🏓 - untuk cek status
• {HNDLR}Id🐵 - untuk melihat id pengguna
• {HNDLR}Video🎬 - judul video | link yt untuk mencari video
• {HNDLR}Song📜 - judul lagu | link yt untuk mencari lagu
• {HNDLR}Help🐣 - untuk melihat daftar perintah


⚡ PERINTAH UNTUK SEMUA ADMIN
• {HNDLR}resume 🐵- untuk melanjutkan pemutaran lagu atau video
• {HNDLR}pause 🐵- untuk untuk menjeda pemutaran lagu atau video
• {HNDLR}skip 🐵- untuk melewati lagu atau video
• {HNDLR}end 🐵- untuk mengakhiri pemutaran</b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>🙈 Ciluk Baaa 🙊 {m.from_user.mention}!

🗃️ Music Dan Video Player UserBot

🔰 Telegram UserBot Untuk Memutar Lagu Dan Video Di Obrolan Suara Telegram.

👩‍💻 Dipersembahkan Oleh 
• [ ](https://t.me/Rafens)


[Source](https://github.com/risswazowlsky/ZaenMusic)
"""
    await m.reply(REPO, disable_web_page_preview=True)
