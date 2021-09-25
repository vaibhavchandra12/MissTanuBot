from config import Config

from pyrogram import Client as kabeercmd

kabeercmd = Client("TG-Bot", bot_token = Config.BOT_TOKEN, api_id = Config.API_ID, api_hash = Config.API_HASH)

kabeercmd.run()
