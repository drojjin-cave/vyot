from aiogram.utils.keyboard import InlineKeyboardBuilder


active_user_menu_dict = {'👤 Профиль': 'профиль',
                    '📜 Инструкции': 'инструкции',
                    '🪙 Тарифы': 'тарифы',
                    '📢 Помощь': 'помощь'}

def user_menu_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='▶️ Попробовать', callback_data='попробовать')
    keyboard_builder.button(text='📜 Инструкции', callback_data='инструкции')
    keyboard_builder.button(text='🪙 Тарифы', callback_data='тарифы')
    keyboard_builder.button(text='📢 Помощь', callback_data='помощь')

    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup()


def keyboard_gen(keyboars, sizes=(2,)):
    keyboard_builder = InlineKeyboardBuilder()
    for text, calback_name in keyboars.items():
        keyboard_builder.button(text=text, callback_data=calback_name)

    keyboard_builder.adjust(*sizes)
    return keyboard_builder.as_markup()

def active_user_menu():
    return keyboard_gen(active_user_menu_dict, (2, 2))