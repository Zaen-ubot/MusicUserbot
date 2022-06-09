# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from MusicUserbot import CMD_HANDLER as cmd
from MusicUserbot import CMD_HELP
from MusicUserbot.utils import 
import random
from MusicUserbot import owner
from pyrogram.tl.types import InputMessagesFilterVideo
from pyrogram.tl.types import InputMessagesFilterVoice


@Client.on_message(filters.command(["asupan"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Gabutnyazaen", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Berhasil menemukan Video**.")
        
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")
