from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main.config import Config
from pyrogram import Client 

@Client.on_message(filters.command('start'))
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Bot Under Beta Testing"""
    ),
 
