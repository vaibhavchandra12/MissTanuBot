from config import Config
from pyrogram import Client as kabeercmd
from pyrogram import filters

log_channel_ = Config.LOG_CHANNEL

async def main_startup():
  await kabeercmd.send_message(chat_id=log_channel_id, text="`Nexa Userbot is started!`")
  await idle()
  
print("Bot Started")
