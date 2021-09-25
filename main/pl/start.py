from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main.config import Config
from pyrogram import Client 

@Client.on_message(filters.command('start'))
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Bot Under Beta Testing"""
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Source", url="https://github.com/vivek-tp/Tg-Bot"),
                    InlineKeyboardButton("Support", url="https://t.me/OpensourceTG")
                ]
            ]
        ),
