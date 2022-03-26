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
async def join_voice_chat(client, message):
    input_filename = os.path.join(
        'input.raw',
    )
        await client. filters.reply('Sudah Bergabung ke Voice Chat 🛠')
        return
    chat_id = message.chat.id
    try:
        group_call = GroupCall(client, input_filename)
        await group_call.start(chat_id)
    except RuntimeError:
        await message.reply('lel error!')
        return
    VOICE_CHATS[chat_id] = group_call
    await message.reply('Bergabung Voice Chat ✅')


@Client.on_message(filters.command(["leavevc"], prefixes=f"{HNDLR}"))
async def leave_voice_chat(client, message):
    chat_id = message.chat.id
    group_call = VOICE_CHATS[chat_id]
    await group_call.stop()
    VOICE_CHATS.pop(chat_id, None)
    await message.reply('Meninggalkan Voice Chat ✅')
