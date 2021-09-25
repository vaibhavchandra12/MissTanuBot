from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
from pyrogram import Client as kabeercmd
from main.text import MSG

@kabeercmd.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=MSG.START_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Source", url="https://github.com/vivek-tp/Tg-Bot"),
                    InlineKeyboardButton("Support", url="https://t.me/OpensourceTG")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )
