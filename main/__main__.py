from main.config import Config

from pyrogram import Client

kabeercmd = Client("TG-Bot", bot_token = Config.BOT_TOKEN, api_id = Config.APP_ID, api_hash = Config.API_HASH)

kabeercmd.run()
