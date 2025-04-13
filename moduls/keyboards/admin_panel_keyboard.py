from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_menu_main_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Активные пользователи', callback_data='пользователи')
    keyboard_builder.button(text='Добавить в ручную', callback_data='добавить_в_ручную')
    keyboard_builder.button(text='Статистика по ID', callback_data='статистика')
    keyboard_builder.button(text='Обновить подписку', callback_data='обновить')
    keyboard_builder.button(text='🔙 Назад', callback_data='назад_из_админки')

    keyboard_builder.adjust(2, 2, 1)
    return keyboard_builder.as_markup()