import asyncio
from aiogram import Bot, Dispatcher
from handlers import greetings
import config

async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_routers(greetings.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    
