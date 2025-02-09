from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNELS

def subscription_keyboard():
    """ Kanallarga obuna bo‘lish uchun tugmalar yaratadi """
    buttons = [
        [InlineKeyboardButton(text=f"📢 {channel.replace('@', '')}", url=f"https://t.me/{channel[1:]}")]
        for channel in CHANNELS
    ]
    buttons.append([InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subscription")])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)
