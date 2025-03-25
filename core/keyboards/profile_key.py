from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.keyboards.reply import keyboard_gen

profile_menu_dict = {'📅 Продлить': 'продлить',
                    '🔀 Поделиться': 'поделиться',
                    '🔙 Назад': 'назад'}

def profile_menu():
    return keyboard_gen(profile_menu_dict)