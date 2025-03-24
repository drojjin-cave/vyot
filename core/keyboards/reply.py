from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def start_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='✅Принять правила использования', callback_data='правила')
    keyboard_builder.button(text='Сами правила тут', url='https://telegram.org/privacy/eu')

    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()


def user_menu_inline():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='▶️ Попробовать', callback_data='попробовать')
    keyboard_builder.button(text='📜 Инструкции', callback_data='инструкции')
    keyboard_builder.button(text='🪙 Тарифы', callback_data='тарифы')
    keyboard_builder.button(text='📢 Помощь', callback_data='помощь')

    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup()

def admin_menu_inline():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='▶️ Попробовать', callback_data='попробовать')
    keyboard_builder.button(text='📜 Инструкции', callback_data='инструкции')
    keyboard_builder.button(text='🪙 Тарифы', callback_data='тарифы')
    keyboard_builder.button(text='📢 Помощь', callback_data='помощь')
    keyboard_builder.button(text='⚙️ Админ-панель', callback_data='админ')

    keyboard_builder.adjust(2, 2, 1)
    return keyboard_builder.as_markup()


def manual_inline():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='📱 Apple', callback_data='айфон')
    keyboard_builder.button(text='📳 Android', callback_data='андроид')
    keyboard_builder.button(text='🔙 Назад', callback_data='назад_из_инструкции')

    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup()


def tarif_inline():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='30 дней - 250 ⭐', callback_data='месяц')
    keyboard_builder.button(text='3 месяца - 700 ⭐', callback_data='3_месяца')
    keyboard_builder.button(text='Полгода - 1300 ⭐', callback_data='полгода')
    keyboard_builder.button(text='Год - 2250 ⭐', callback_data='год')
    keyboard_builder.button(text='🔙 Назад', callback_data='назад_из_тарифов')

    keyboard_builder.adjust(2, 2, 1)
    return keyboard_builder.as_markup()


def android_inline():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🔙 Назад', callback_data='назад_из_андроид')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

