from aiogram import Bot
from aiogram.types import Message, FSInputFile
from core.keyboards.reply import start_keyboard, user_menu_inline
from core.utils.dbconnect import get_user, check_db
import core.utils.manuals as manuals


async def get_start(message: Message, bot: Bot):
    photo = "core/pictures/vpn.jpg"
    await check_db()

    #await bot.send_photo(message.from_user.id, photo=FSInputFile(path=photo), caption=text, reply_markup=user_menu_inline())
    check = await get_user(message.from_user.id)
    if check is None:
        await message.answer(f'Для продолжения работы необходимо принять условия использования', reply_markup=start_keyboard())
    else:
        await bot.send_photo(message.from_user.id, photo=FSInputFile(path=photo), caption=manuals.TEXT_START, reply_markup=user_menu_inline())

