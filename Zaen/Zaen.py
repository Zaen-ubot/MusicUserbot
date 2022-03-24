from random import randint
from pyrogram import Client, filters
from config import HNDLR, bot as USER
from Zaen.helpers.decorators import authorized_users_only
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram import GroupCallFactory
from pyrogram import GroupCall

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


@Client.on_message(filters.command(["opengc"], prefixes=f"{HNDLR}"))
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
async def joinvc(client, filters):
    info={
        "header": "join voice chat group.",
        "description": "To join voice chat group.",
        "usage": "{tr}joinvc",
        "note": "make sure voice chat is active",
    },

async def start(_, message: Message):
    group_call = getchat
    await group_call.start(message.chat.id)

async def join_voice_chat(client, message):
    if message.chat.id in getchat:
        await message.reply('Already joined to Voice Chat')
        return
    chat_id = message.chat.id
    try:
        group_call = GroupCall(client, message)
        await group_call.start(chat_id)
    except RuntimeError:
        await message.reply('error!')
        return
    getchat[chat_id] = group_call
    await message.reply('Joined the Voice Chat ')
