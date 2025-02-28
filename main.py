from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import logging


from core.handlers.basic import *
import asyncio
from core.settings import settings


from core.handlers.callback import *
from core.utils.comands import set_commands

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')

# тест коммита 2
async def start():
    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, CommandStart())

    # Главное меню
    dp.callback_query.register(select_ruls, F.data == 'правила')

    dp.callback_query.register(select_test, F.data == 'попробовать')
    dp.callback_query.register(select_manual, F.data == 'инструкции')
    dp.callback_query.register(select_tarif, F.data == 'тарифы')
    dp.callback_query.register(select_help, F.data == 'помощь')

    # кнопки возврата
    dp.callback_query.register(back_from_manual, F.data == 'назад_из_инструкции')

    # меню инструкций
    dp.callback_query.register(manual_android, F.data == 'андроид')



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
