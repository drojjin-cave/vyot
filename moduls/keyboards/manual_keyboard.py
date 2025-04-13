from aiogram.utils.keyboard import InlineKeyboardBuilder


def manual_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='📱 Apple', callback_data='айфон')
    keyboard_builder.button(text='📳 Android', callback_data='андроид')
    keyboard_builder.button(text='🔙 Назад', callback_data='назад')

    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup()


def back_from_manuals_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🔙 Назад', callback_data='назад_из_инструкций')
    return keyboard_builder.as_markup()