from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile
from core.keyboards.admin_panel import admin_menu_main_inline
from core.keyboards.reply import user_menu_inline, admin_menu_inline



async def get_active_users(call: CallbackQuery, bot: Bot):
    '''Активные пользователи'''

    #await call.message.answer('здесь что-то про оплату за месяц') TODO: Понять,что нужно делать при оплате 1 месяц


    await call.answer()


async def back_from_admin(call: CallbackQuery, bot: Bot):

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=admin_menu_inline())

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