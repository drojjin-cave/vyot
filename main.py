from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import logging
from core.utils.x3_UI import X3_UI


from core.handlers.basic import *
import asyncio
from core.settings import settings


from core.handlers.callback import *
from core.utils.comands import set_commands
from core.handlers.callback_tarif import *
from core.handlers.callback_admin import *

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
    dp.callback_query.register(select_admin, F.data == 'админ')

    # кнопки возврата
    dp.callback_query.register(back_from_manual, F.data == 'назад_из_инструкции')
    dp.callback_query.register(back_from_tarif, F.data == 'назад_из_тарифов')
    dp.callback_query.register(back_from_android, F.data == 'назад_из_андроид')
    dp.callback_query.register(back_from_admin, F.data == 'назад_из_админки')

    # меню инструкций
    dp.callback_query.register(manual_android, F.data == 'андроид')
    dp.callback_query.register(manual_apple, F.data == 'айфон')

    #тарифы
    dp.callback_query.register(month_pay, F.data == 'месяц')
    dp.callback_query.register(thre_month_pay, F.data == '3_месяца')
    dp.callback_query.register(six_month_pay, F.data == 'полгода')
    dp.callback_query.register(year_pay, F.data == 'год')

    #админ панель
    dp.callback_query.register(get_active_users, F.data == 'пользователи')
    dp.callback_query.register(add_user_hand, F.data == 'добавить_в_ручную')
    dp.callback_query.register(static_of_user, F.data == 'статистика')
    dp.callback_query.register(update_time_of_user, F.data == 'обновить')




    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())
