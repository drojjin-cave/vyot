from aiogram import Bot
from aiogram.types import Message
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from core.utils.dbconnect import add_user
from core.keyboards.reply import user_menu_inline, manual_inline, tarif_inline, android_inline, active_user_menu
from core.keyboards.admin_panel import admin_menu_main_inline
import core.utils.manuals as manuals
from core.handlers.basic import server

photo = "core/pictures/vpn.jpg"
async def select_ruls(call: CallbackQuery, bot: Bot):
    data = call.data
    connect = await add_user(call.from_user.id, call.from_user.first_name)
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=None)


    if connect:
        await bot.send_photo(call.from_user.id, photo=FSInputFile(path=photo), caption=manuals.TEXT_START, reply_markup=user_menu_inline())
    else:
        await call.message.answer('Что-то пошло не так')

    await call.answer()


async def select_test(call: CallbackQuery, bot: Bot):

    #await call.message.answer('Тут профиль') TODO: доделать тестовый период
    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)

    await call.answer()


async def select_admin(call: CallbackQuery, bot: Bot):
    #await bot.edit_message_text(chat_id=message.chat.id, message_id=mymessage.message_id, text="Lorem Ipsum is a dummy")
    #await call.message.edit_media(media=InputMediaPhoto(media=photo, caption='Админ панель'), reply_markup=admin_menu_main_inline())
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=admin_menu_main_inline())
    #await call.message.answer('Тут профиль') TODO: доделать тестовый период
    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)

    await call.answer()


async def select_manual(call: CallbackQuery, bot: Bot):

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=manual_inline())

    await call.answer()

async def back_from_manual(call: CallbackQuery, bot: Bot):
    check = server.check_user(call.from_user.id)
    if not check:
        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                            reply_markup=user_menu_inline())
    else:
        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                            reply_markup=active_user_menu())

    await call.answer()

async def select_tarif(call: CallbackQuery, bot: Bot):
    '''Выбор тарифа'''
    #photo = "core/pictures/tarif.jpg"

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=tarif_inline())
    #await call.message.answer_photo(photo=FSInputFile(path=photo), caption='Выберите срок использования', reply_markup=tarif_inline())

    await call.answer()


async def back_from_tarif(call: CallbackQuery, bot: Bot):
    check = server.check_user(call.from_user.id)
    if not check:
        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                            reply_markup=user_menu_inline())
    else:
        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                            reply_markup=active_user_menu())

    await call.answer()

async def select_help(call: CallbackQuery, bot: Bot):

    #await call.message.answer('Здесь помощь asdf') #TODO: Доделать помощь

    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)

    await call.answer()


async def manual_android(call: CallbackQuery, bot: Bot):
    '''Инструкция андроид'''
    photo = "core/pictures/android-logo.jpg"
    await call.message.answer_photo(photo=FSInputFile(path=photo), caption=manuals.MANUAL_ANDROID, reply_markup=android_inline())

    await call.answer()


async def manual_apple(call: CallbackQuery, bot: Bot):
    '''Инструкция айфон'''
    photo = "core/pictures/apple-logo.png"
    await call.message.answer_photo(photo=FSInputFile(path=photo), caption=manuals.MANUAL_APPLE, reply_markup=android_inline())


    await call.answer()


async def back_from_android(call: CallbackQuery, bot: Bot):
    await call.message.delete()
    #await bot.edit_message_caption(chat_id=call.from_user.id, message_id=call.message.message_id, caption='asdf')
    #await bot.edit_message_media(chat_id=call.from_user.id, message_id=call.message.message_id, media='')
    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=manual_inline())



    await call.answer()

