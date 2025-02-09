from aiogram import Bot
from aiogram.types import ChatMember

# API tokenni o'z botingniki bilan almashtir
BOT_TOKEN = "7267295704:AAFa5cS0bskZGjiY4XISVfGClzcIpgifb08"

# Tekshiriladigan kanallar ro'yxati (o'zingga kerakli kanallarni yoz)
CHANNELS = [
    "@tekin_dasturlar",
    "@dasturlar_uzb3",
]

async def check_subscriptions(bot: Bot, user_id: int):
    """Foydalanuvchi barcha kanallarga obuna bo‘lganmi yoki yo‘q, tekshiradi."""
    not_subscribed = []

    for channel in CHANNELS:
        try:
            chat_member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if chat_member.status not in [ChatMember.MEMBER, ChatMember.OWNER, ChatMember.ADMINISTRATOR]:
                not_subscribed.append(channel)
        except Exception as e:
            print(f"Xatolik {channel} kanalida: {e}")
            not_subscribed.append(channel)

    return not_subscribed

async def main():
    bot = Bot(token=BOT_TOKEN)
    user_id = int(input("Foydalanuvchi ID sini kiriting: "))  # Foydalanuvchi ID sini kiritish
    not_subscribed = await check_subscriptions(bot, user_id)

    if not_subscribed:
        print("❌ Foydalanuvchi quyidagi kanallarga obuna bo‘lmagan:")
        for channel in not_subscribed:
            print(f"👉 {channel}")
    else:
        print("✅ Foydalanuvchi barcha kanallarga obuna bo‘lgan!")

import asyncio
asyncio.run(main())
