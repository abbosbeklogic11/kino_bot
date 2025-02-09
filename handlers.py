from aiogram import Router, types
from aiogram.filters import Command
from utils import check_subscriptions
from keyboards import subscription_keyboard
from database import get_movie_by_code

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    is_subscribed = await check_subscriptions(user_id)

    if not is_subscribed:
        text = "🚨 Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:"
        await message.answer(text, reply_markup=subscription_keyboard())
        return
    
    await message.answer("✅ Siz barcha kanallarga obuna bo‘lgansiz! Endi kino kodini kiriting:")

@router.callback_query(lambda call: call.data == "check_subscription")
async def check_subscription_callback(call: types.CallbackQuery):
    """ Foydalanuvchi obunasini qayta tekshiradi """
    user_id = call.from_user.id
    is_subscribed = await check_subscriptions(user_id)

    if not is_subscribed:
        text = "🚫 Siz hali hamma kanallarga obuna bo‘lmadingiz! Iltimos, obuna bo‘ling."
        await call.message.edit_text(text, reply_markup=subscription_keyboard())
    else:
        await call.message.edit_text("✅ Siz barcha kanallarga obuna bo‘lgansiz! Endi kino kodini kiriting:")

@router.message()
async def movie_handler(message: types.Message):
    """ Kino kodini tekshirish """
    movie_code = message.text.strip()
    movie_info = get_movie_by_code(movie_code)

    if movie_info:
        await message.answer(f"🎬 Kino topildi!\n\n{movie_info}")
    else:
        await message.answer("🚫 Bunday kino topilmadi. Iltimos, kodni to‘g‘ri kiriting.")
