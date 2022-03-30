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
@authorized_users_only
async def join_voice_chat(client, m: Message):
    command = m.command
    len_command = len(command)
    if 2 <= len_command <= 4:
        channel = await get_id(command[1])
        join_as = await get_id(command[2]) if len_command >= 3 else None
        invite_hash = command[3] if len_command == 4 else None
        group_call = mp.group_call
        group_call.client = client
        if group_call.is_connected:
            text = f"{emoji.ROBOT} already joined a voice chat"
        else:
            await group_call.start(channel, join_as=join_as,
                                   invite_hash=invite_hash)
