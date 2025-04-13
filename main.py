import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from moduls.handlers.basic import basic_handlers
from moduls.handlers.paymant import payment_messages_handlers
from moduls.handlers.manuals import manuals_handlers
from moduls.handlers.profile import profile_handlers

from moduls.settings import settings

dp = Dispatcher()

async def main():
    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.include_routers(basic_handlers,
                       profile_handlers,
                       payment_messages_handlers,
                       manuals_handlers
                       )

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s : [%(levelname)s] [%(name)s] : %(message)s")
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    asyncio.run(main())
