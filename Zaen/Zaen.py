import os

from random import randint
from pyrogram import Client, filters
from config import HNDLR, bot as USER
from Zaen.helpers.decorators import authorized_users_only
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.raw.functions.phone import CreateGroupCall


@Client.on_message(filters.command(["join"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def join(client, message):
    chat_id = message.chat.id
    try:
        link = await client.export_chat_invite_link(chat_id)
    except BaseException:
        await message.reply("**Error:**\nTambahkan saya sebagai admin grup Anda!")
        return
    try:
        await USER.join_chat(link)
        await message.reply("**Userbot Joined**")
    except UserAlreadyParticipant:
        await message.reply("**Userbot Udah join Disini**")


@Client.on_message(filters.command(["openvcs"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def opengc(client, message):
    flags = " ".join(message.command[1:])
    if flags == "channel":
        chat_id = message.chat.title
        type = "channel"
    else:
        chat_id = message.chat.id
        type = "group"
    try:
        await USER.send(CreateGroupCall(
            peer=(await USER.resolve_peer(chat_id)),
            random_id=randint(10000, 999999999)
        )
        )
    except Exception:
        await message.reply(
            "**Error:** Add userbot as admin of your group/channel with permission **Can manage voice chat**"
        )

@Client.on_message(filters.command(["joinvc"], prefixes=f"{HNDLR}"))
async def join_(event):
    geezav = await edit_or_reply(event, f"**Processing**")
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client(GetFullUserRequest(chat))
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return await edit_or_reply(event, "NodeJs is not installed or installed version is too old.")
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat)
            await asyncio.sleep(3)
        except Exception as e:
            return await botman.delete(f'Error during Joining the Call\n`{e}`')
    else:
        chat = event.chat_id
        from_user = vcmention(event.sender)
    if not call_py.is_connected:
        await call_py.start()
    await call_py.join_group_call(
        chat,
        AudioPiped(
            'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
        ),
        stream_type=StreamType().pulse_stream,
    )
    await botman.edit(f"**{from_user} Berhasil Naik Ke VC Group!!!**")


@Client.on_message(filters.command(["leavevc"], prefixes=f"{HNDLR}"))
async def leavevc(event):
    """ leave video chat """
    botman = await edit_or_reply(event, "Processing")
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if from_user:
        try:
            await call_py.leave_group_call(chat_id)
        except (NotInGroupCallError, NoActiveGroupCall):
            pass
        await botman.edit(f"**{from_user} Berhasil Turun Dari VC Group!!**")
    else:
        await botman.delete(f"**Maaf {from_user} Tidak Berada Di VC Group**")
