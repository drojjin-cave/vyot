from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile
from core.keyboards.reply import user_menu_inline, manual_inline, tarif_inline



async def month_pay(call: CallbackQuery, bot: Bot):
    '''Оплата месяц'''
    #photo = "core/pictures/apple-logo.png"

    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    #await call.message.answer_photo(photo=FSInputFile(path=photo), caption=manuals.MANUAL_APPLE, reply_markup=manual_inline())
    await call.message.answer('здесь что-то про оплату за месяц')


    await call.answer()


async def thre_month_pay(call: CallbackQuery, bot: Bot):
    '''Оплата 3 месяца'''
    #photo = "core/pictures/apple-logo.png"

    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    #await call.message.answer_photo(photo=FSInputFile(path=photo), caption=manuals.MANUAL_APPLE, reply_markup=manual_inline())
    await call.message.answer('здесь что-то про оплату за 3 месяца')


    await call.answer()


async def six_month_pay(call: CallbackQuery, bot: Bot):
    '''Оплата 6 месяцев'''
    #photo = "core/pictures/apple-logo.png"

    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    #await call.message.answer_photo(photo=FSInputFile(path=photo), caption=manuals.MANUAL_APPLE, reply_markup=manual_inline())
    await call.message.answer('здесь что-то про оплату за пол года')


    await call.answer()



async def year_pay(call: CallbackQuery, bot: Bot):
    '''Оплата за год'''
    #photo = "core/pictures/apple-logo.png"

    #await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=None)
    #await call.message.answer_photo(photo=FSInputFile(path=photo), caption=manuals.MANUAL_APPLE, reply_markup=manual_inline())
    await call.message.answer('здесь что-то про оплату за год')


    await call.answer()