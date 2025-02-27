from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Кнопка 1')
    keyboard_builder.button(text='Кнопка 2')
    keyboard_builder.button(text='Кнопка 3')

    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def register_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Регистрация')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def start_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='✅Принять правила использования', callback_data='правила')
    keyboard_builder.button(text='Сами правила тут', url='https://telegram.org/privacy/eu')

    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def user_menu_inline():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='▶️ Попробовать', callback_data='профиль')
    keyboard_builder.button(text='📜 Инструкции', callback_data='тест')
    keyboard_builder.button(text='🪙 Тарифы', callback_data='инфо')
    keyboard_builder.button(text='📢 Помощь', callback_data='тарифы')

    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup()


def user_menu_reply():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='👤Профиль')
    keyboard_builder.button(text='⏳Тестовый период')
    keyboard_builder.button(text='ℹОбщая информация')
    keyboard_builder.button(text='🪙Тарифы')

    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True)