from aiogram import Bot
from aiogram.types import ChatMember
from config import TOKEN, CHANNELS

bot = Bot(token=TOKEN)

async def check_subscriptions(user_id: int) -> bool:
    """ Foydalanuvchining barcha kanallarga obuna bo‘lganini tekshiradi """
    for channel in CHANNELS:
        try:
            chat_member = await bot.get_chat_member(channel, user_id)
            if chat_member.status not in ["member", "administrator", "creator"]:
                return False
        except Exception as e:
            print(f"❌ Xato: {e}")  # Debug uchun
            return False
    return True
