from aiogram.utils.keyboard import InlineKeyboardBuilder

def tarif_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='30 дней - 250 ⭐', callback_data='месяц')
    keyboard_builder.button(text='3 месяца - 700 ⭐', callback_data='3 месяца')
    keyboard_builder.button(text='6 месяцев - 1300 ⭐', callback_data='6 месяцев')
    keyboard_builder.button(text='Год - 2250 ⭐', callback_data='год')
    keyboard_builder.button(text='Тест - 1 ⭐', callback_data='тест')
    keyboard_builder.button(text='🔙 Назад', callback_data='назад')

    keyboard_builder.adjust(2, 2, 1, 1)
    return keyboard_builder.as_markup()



def pay_month_keyboard(price):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text=f'✅ Оплатить', pay=True)
    keyboard_builder.button(text='❌ Отменить', callback_data='отменить_оплату')
    keyboard_builder.adjust(2,)

    return keyboard_builder.as_markup()