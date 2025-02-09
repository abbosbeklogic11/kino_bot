from aiogram import Bot, Dispatcher
import asyncio
from handlers import router

TOKEN = "7267295704:AAFa5cS0bskZGjiY4XISVfGClzcIpgifb08"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    dp.include_router(router)

    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
