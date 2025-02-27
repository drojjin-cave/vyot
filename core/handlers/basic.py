from aiogram import Bot
from aiogram.types import Message, FSInputFile
from core.keyboards.reply import get_reply_keyboard, register_keyboard, start_keyboard, user_menu_inline, user_menu_reply
from core.utils.dbconnect import get_user

text = """
Добро пожаловать!

Возможности:
Смотрите YouTube в 4K без задержек
Неограниченный трафик и высокая скорость
Полная анонимность
Доступ к заблокированным сайтам и сервисам
Подключение за 1 клик без сложных настроек
"""


async def get_start(message: Message, bot: Bot):
    photo = "core/pictures/vpn.jpg"



    #await bot.send_photo(message.from_user.id, photo=FSInputFile(path=photo), caption=text, reply_markup=user_menu_inline())
    check = await get_user(message.from_user.id)
    if check is None:
        await message.answer(f'Для продолжения работы необходимо принять условия использования', reply_markup=start_keyboard())
    else:
        await bot.send_photo(message.from_user.id, photo=FSInputFile(path=photo), caption=text, reply_markup=user_menu_inline())

# тест

async def knopka1(message: Message, bot: Bot):
    await message.answer(f'Действие по кнопке 1', reply_markup=get_reply_keyboard())

async def knopka2(message: Message, bot: Bot):
    await message.answer(f'Действие по кнопке 2', reply_markup=get_reply_keyboard())

async def knopka3(message: Message, bot: Bot):
    await message.answer(f'Действие по кнопке 3', reply_markup=get_reply_keyboard())