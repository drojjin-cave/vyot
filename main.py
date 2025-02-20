from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import F


from core.handlers.basic import *
import asyncio
from core.settings import settings


from core.handlers.callback import *
from core.utils.comands import set_commands

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def test(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Тест!')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')

# еще тест



async def start():
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # регистрация команд и фильтр по нажатию кнопок
    dp.message.register(get_start, CommandStart())
    dp.message.register(knopka1, F.text == 'Кнопка 1')
    dp.message.register(knopka2, F.text == 'Кнопка 2')
    dp.message.register(knopka3, F.text == 'Кнопка 3')

    dp.callback_query.register(select_ruls, F.data == 'правила')
    dp.callback_query.register(select_profile, F.data == 'профиль')
    dp.callback_query.register(select_test, F.data == 'тест')
    dp.callback_query.register(select_info, F.data == 'инфо')
    dp.callback_query.register(select_tarif, F.data == 'тарифы')


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
