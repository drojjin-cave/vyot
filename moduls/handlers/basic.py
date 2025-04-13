from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart
import logging
from moduls.utils.static_text import TEXT_START
from moduls.keyboards.main_keyboard import *

from moduls.utils.comands import set_commands
from moduls.utils.static_text import MAIN_PHOTO_PATH
from moduls.utils.x3_UI import X3_UI
from moduls.settings import settings

ADMINS_VPN = settings.bots.admins_vpn


basic_handlers = Router(name=__name__)
server = X3_UI()

@basic_handlers.message(CommandStart())
async def get_start(message: Message, bot: Bot):
    await set_commands(bot, message.from_user.id)

    check = server.check_user(message.from_user.id)
    if not check:
        await bot.send_photo(message.from_user.id, photo=FSInputFile(path=MAIN_PHOTO_PATH), caption=TEXT_START, reply_markup=user_menu_keyboard())
    else:
        await bot.send_photo(message.from_user.id, photo=FSInputFile(path=MAIN_PHOTO_PATH), caption=TEXT_START, reply_markup=active_user_menu())


    logging.info(f'Пользователь {message.from_user.username} {message.from_user.id} нажал кнопку "СТАРТ"')


@basic_handlers.callback_query(F.data == 'назад')
async def back_from_tarif(call: CallbackQuery, bot: Bot):

    check = server.check_user(call.from_user.id)
    if not check:
        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                            reply_markup=user_menu_keyboard())
    else:
        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                            reply_markup=active_user_menu())

    await call.answer()
