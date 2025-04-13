from aiogram import Bot, Router
from aiogram.types import CallbackQuery, FSInputFile, Message
from moduls.keyboards.admin_panel_keyboard import admin_menu_main_keyboard
from aiogram.filters import Command

from moduls.settings import settings
from moduls.utils.static_text import MAIN_PHOTO_PATH

from datetime import datetime, timedelta, timezone
ADMINS_VPN = settings.bots.admins_vpn


admin_handlers = Router(name=__name__)

@admin_handlers.message(Command("logs"))
async def send_logs(message: Message, bot:Bot,  n=30):
    n = int("-" + str(n))
    log = r'/home/drojjin/.pm2/logs/tg-vyot-error.log'

    date_update_info = datetime.now(timezone.utc)
    date_update_info = (date_update_info + timedelta(hours=7, minutes=0)).strftime('%d-%m-%Y %H-%M')

    log_out = f'/home/drojjin/.pm2/logs/tg-vyot-logs/{date_update_info}.log'

    log_local = r'C:\Users\Admin\Desktop\Документы\!BOTS\vyot-bot\vyot\tg-vyot-error.log'
    log_local_out = f'C:\\Users\\Admin\\Desktop\Документы\\!BOTS\\vyot-bot\\vyot\\{date_update_info}.log'

    await message.delete()
    if message.from_user.id in ADMINS_VPN:
        with open(log, mode="r") as logs:
            logs = logs.readlines()
        with open(log_out, mode='w') as logs_out:
            logs_out.write("".join(logs[-1:n:-1]))
        await message.answer_document(document=FSInputFile(path=log_out), caption='Логи')

async def get_active_users(call: CallbackQuery, bot: Bot):
    '''Активные пользователи'''

    #await call.message.answer('здесь что-то про оплату за месяц') TODO: Понять,что нужно делать при оплате 1 месяц


    await call.answer()


async def back_from_admin(call: CallbackQuery, bot: Bot):

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=admin_menu_main_keyboard())

    await call.answer()
async def add_user_hand(call: CallbackQuery, bot: Bot):
    '''Добавить в ручную'''

    #await call.message.answer('здесь что-то про оплату за месяц') TODO: Понять,что нужно делать при оплате 1 месяц


    await call.answer()


async def static_of_user(call: CallbackQuery, bot: Bot):
    '''Статистика пользователя'''

    #await call.message.answer('здесь что-то про оплату за месяц') TODO: Понять,что нужно делать при оплате 1 месяц


    await call.answer()

async def update_time_of_user(call: CallbackQuery, bot: Bot):
    '''Обновить подписку'''

    #await call.message.answer('здесь что-то про оплату за месяц') TODO: Понять,что нужно делать при оплате 1 месяц


    await call.answer()