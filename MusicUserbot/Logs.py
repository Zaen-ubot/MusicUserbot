import os

from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import ADMINS


@Bot.on_message(filters.command("logs") & filters.user(ADMINS))
async def get_bot_logs(client: Bot, m: Message):
    bot_log_path = "logs.txt"
    if os.path.exists(bot_log_path):
        try:
            await m.reply_document(
                bot_log_path,
                quote=True,
                caption="<b>Ini Logs Bot ini</b>",
            )
        except Exception as e:
            os.remove(bot_log_path)
            print(f"[ERROR]: {e}")
    else:
        if not os.path.exists(bot_log_path):
            await m.reply_text("❌ <b>Tidak ada log yang ditemukan!</b>")
