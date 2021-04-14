from pyrogram import Client, filters
from pyromod import listen
from .config import Config
import logging
import datetime
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from .handlers.commands import StartHandler, set_all_handler, set_admin_only_handler, delete_message,cancel
from .handlers.group import add_group, remove_group
from .handlers.mention import admin_tag, all_tag

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot = Client('bot', api_id=Config.TELEGRAM_APP_ID,
                api_hash=Config.TELEGRAM_APP_HASH, bot_token=Config.TELEGRAM_TOKEN)

bot.add_handler(MessageHandler(
    StartHandler, filters.private & filters.command(['start'])))
bot.add_handler(MessageHandler(set_all_handler,
                                 filters.command(['set_all'])))
bot.add_handler(MessageHandler(set_admin_only_handler,
                                filters.command(['set_admin_only'])))
bot.add_handler(MessageHandler(delete_message, 
                                filters.command(['delete_all'])))
bot.add_handler(MessageHandler(cancel, 
                                filters.command(['cancel'])))
bot.add_handler(MessageHandler(add_group, filters.private &
                                filters.regex('^➕ Add Group$')))
bot.add_handler(MessageHandler(remove_group, filters.private &
                                filters.regex('^➖ Remove Group$')))
bot.add_handler(MessageHandler(
    all_tag, filters.regex('^@all$')))
bot.add_handler(MessageHandler(
    admin_tag, filters.regex('^@admin$')))
