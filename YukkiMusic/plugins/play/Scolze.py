import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","مطور السورس","المطور","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg",
         caption=f"""◍ مش محتاجين نكتب كلام كتير خش ع اول زرار وانت هتعرف""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("• 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ☤ ", url=f"https://t.me/WORLD_MUSIC_F"),
            ],
            [
                InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )
