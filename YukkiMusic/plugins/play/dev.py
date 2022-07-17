import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_DEV1 = getenv("IMG_DEV1")

OWNER = getenv("OWNER")

OWNER_NAME = getenv("OWNER_NAME")



@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg",
        caption=f"""ᴘʀᴏɢʀᴀᴍᴍᴇʀ [𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ☤ ](https://t.me/WORLD_MUSIC_F) 𖡼\nᴛᴏ ᴄᴏᴍᴍụɴɪᴄᴀᴛᴇ ᴛᴏɢᴇᴛʜᴇʀ 𖡼\nғᴏʟʟᴏᴡ ᴛʜᴇ ʙụᴛᴛᴏɴѕ ʟᴏᴡᴇʀ 𖡼""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("♡اضف البوت الى مجموعتك♡", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )
