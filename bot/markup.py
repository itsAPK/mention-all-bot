from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            KeyboardButton, ReplyKeyboardMarkup,
                            ReplyKeyboardRemove)


def start_markup():
    return ReplyKeyboardMarkup([[
        KeyboardButton("➕ Add Group"),
        KeyboardButton("➖ Remove Group")
    ]])
    
    
    