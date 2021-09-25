from main.config import Config

from pyrogram import Client

Client = Client("TG-Bot", bot_token = Config.BOT_TOKEN, api_id = Config.API_ID, api_hash = Config.API_HASH)

Client.run()
#ntg
