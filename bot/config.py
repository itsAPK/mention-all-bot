import os

from dotenv import load_dotenv

load_dotenv()



class Config:
    DATABASE_URI=os.environ.get('DATABASE_URI',None)
    TELEGRAM_TOKEN=os.environ.get('TELEGRAM_TOKEN',None)
    BOT_USERNAME=os.environ.get('BOT_USERNAME',None)
    TELEGRAM_APP_HASH=os.environ.get('TELEGRAM_APP_HASH',None)
    TELEGRAM_APP_ID=os.environ.get('TELEGRAM_APP_ID',None)
    BOT_NAME=os.environ.get('BOT_NAME',None)
    ADMIN_ID=[431108047,552376726]
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')

    if not BOT_USERNAME:
        raise ValueError('BOT USERNAME not set')

    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    
    if not BOT_NAME:
        raise ValueError("BOT NAME not set")
    
    if not ADMIN_ID:
        raise ValueError('ADMIN ID not set')
    
