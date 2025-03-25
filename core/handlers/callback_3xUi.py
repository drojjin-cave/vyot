from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from core.handlers.basic import server
from core.keyboards.profile_key import profile_menu

photo = "core/pictures/vpn.jpg"

async def select_test(call: CallbackQuery, bot: Bot):
    days = 3
    user = 'client-' + call.from_user.username + '-free'
    server.add_client(days, call.from_user.id, user)
    data = server.get_emails_user(call.from_user.id)
    answer = 'Приятного пользования!👽\n\n' + server.print_stat(data[0])
    await call.message.edit_media(InputMediaPhoto(media=FSInputFile(path=photo), caption=answer),
                                  reply_markup=profile_menu())

    await call.answer()


async def renew(call: CallbackQuery, bot: Bot):
    await call.answer()


async def share(call: CallbackQuery, bot: Bot):
    await call.answer()