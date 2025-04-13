import asyncio

from aiogram import Router, F, Bot
from aiogram.types import LabeledPrice, PreCheckoutQuery, CallbackQuery, Message, FSInputFile
from aiogram.filters import Command, CommandObject

from moduls.keyboards.main_keyboard import active_user_menu
from moduls.utils.static_text import PAY_MONTH, MAIN_PHOTO_PATH, TEXT_START
from moduls.keyboards.pay_keyboards import pay_month_keyboard, tarif_keyboard


import logging

PRICES = {'месяц': 250, '3 месяца': 750, '6 месяцев': 1300, 'год': 2250, 'тест': 1}

payment_messages_handlers = Router(name=__name__)
CURRENCY = 'XTR'

@payment_messages_handlers.callback_query(F.data == 'тарифы')
async def select_tarif(call: CallbackQuery, bot: Bot):
    '''Выбор тарифа'''
    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        reply_markup=tarif_keyboard())
    await call.answer()



@payment_messages_handlers.callback_query(F.data.in_(PRICES))
async def select_subscribe(call: CallbackQuery):
    '''Оплата подписки'''
    price = PRICES[call.data]
    global mes
    mes = await call.message.edit_reply_markup()

    global pay_mes
    pay_mes = await call.message.answer_invoice(
        title='Оплата тарифа',
        description=PAY_MONTH,
        prices=[LabeledPrice(label=call.data, amount=price)],
        provider_token="",
        payload=call.data,
        currency=CURRENCY, reply_markup=pay_month_keyboard(price))

    logging.info(f'Пользователь {call.from_user.username} {call.from_user.id} выбрал оплату тарифа "{call.data.upper()}"')
    await call.answer()


@payment_messages_handlers.message(Command("refund"))
async def back_payment(message: Message, bot: Bot, command: CommandObject):
    transaction_id = command.args
    await message.delete()
    try:
       await bot.refund_star_payment(
            user_id=message.from_user.id,
            telegram_payment_charge_id=transaction_id
        )

    except Exception as e:
        print(e)





@payment_messages_handlers.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await pre_checkout_query.answer(ok=True)


@payment_messages_handlers.message(F.successful_payment)
async def process_successful_payment(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=pay_mes.message_id)

    logging.info(f'Пользователь {message.from_user.username} {message.from_user.id} оплатил тариф "{message.successful_payment.invoice_payload.upper()}"')

    curent_subscribe = message.successful_payment.invoice_payload
    text = f'<blockquote>Поздравляем, вы успешно оплатили подписку на <b>{curent_subscribe}</b>!</blockquote>'

    await bot.edit_message_caption(chat_id=message.chat.id, message_id=mes.message_id, caption=text)

    #await message.answer(text, message_effect_id="5104841245755180586")
    await asyncio.sleep(3)
    await bot.edit_message_caption(chat_id=message.chat.id, message_id=mes.message_id, caption=TEXT_START, reply_markup=active_user_menu())



@payment_messages_handlers.callback_query(F.data == 'отменить_оплату')
async def cancel_payment(call: CallbackQuery, bot: Bot):
    await call.message.delete()
    await bot.edit_message_reply_markup(message_id=mes.message_id, reply_markup=tarif_keyboard(), chat_id=call.from_user.id)
    await call.answer()
