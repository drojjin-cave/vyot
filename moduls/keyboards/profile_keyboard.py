from aiogram.utils.keyboard import InlineKeyboardBuilder
from moduls.keyboards.main_keyboard import keyboard_gen

profile_menu_dict = {'📅 Продлить': 'продлить',
                    '🔀 Поделиться': 'поделиться',
                    '🔙 Назад': 'назад из профиля'}

def profile_menu():
    return keyboard_gen(profile_menu_dict)