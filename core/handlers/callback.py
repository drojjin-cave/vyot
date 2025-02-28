from aiogram import Bot
from aiogram.types import Message
from aiogram.types import CallbackQuery, FSInputFile
from core.utils.dbconnect import add_user
from core.keyboards.reply import user_menu_inline, manual_inline
import core.utils.manuals as manuals


text = """
Добро пожаловать!

Возможности:
Смотрите YouTube в 4K без задержек
Неограниченный трафик и высокая скорость
Полная анонимность
Доступ к заблокированным сайтам и сервисам
Подключение за 1 клик без сложных настроек
"""


async def select_ruls(call: CallbackQuery, bot: Bot):
    data = call.data
    connect = await add_user(call.from_user.id, call.from_user.first_name)
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=None)
    photo = "core/pictures/vpn.jpg"

    if connect:
        await bot.send_photo(call.from_user.id, photo=FSInputFile(path=photo), caption=text, reply_markup=user_menu_inline())
    else:
        await call.message.answer('Что-то пошло не так')

    await call.answer()


async def select_test(call: CallbackQuery, bot: Bot):

    await call.message.answer('Тут профиль')
    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)

    await call.answer()


async def select_manual(call: CallbackQuery, bot: Bot):

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=manual_inline())

    await call.answer()

async def back_from_manual(call: CallbackQuery, bot: Bot):

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=user_menu_inline())

    await call.answer()

async def select_tarif(call: CallbackQuery, bot: Bot):

    await call.message.answer('Здесь информация')
    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)

    await call.answer()

async def select_help(call: CallbackQuery, bot: Bot):

    await call.message.answer('А здесь тарифы')
    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)

    await call.answer()


async def manual_android(call: CallbackQuery, bot: Bot):
    '''Инструкция андроид'''

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    await call.message.answer(manuals.MANUAL_ANDROID, reply_markup=manual_inline())


    await call.answer()

