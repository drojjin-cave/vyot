from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from moduls.handlers.basic import server
from moduls.keyboards.main_keyboard import keyboard_gen, active_user_menu
from moduls.keyboards.profile_keyboard import profile_menu
from moduls.utils.static_text import MAIN_PHOTO_PATH, TEXT_START


profile_handlers = Router(name=__name__)

@profile_handlers.callback_query(F.data == "попробовать")
async def select_test(call: CallbackQuery, bot: Bot):
    days = 3
    if call.from_user.username:
        user = 'client-' + call.from_user.username + '-free'
    else:
        user = 'client-' + call.from_user.first_name.replace(' ', '_') + '-free'
    server.add_client(days, call.from_user.id, user)
    data = server.get_emails_user(call.from_user.id)
    answer = ('Приятного пользования!👽\n\n' + 'Кликни на ссылку ниже и переходи к инструкциям😏\n\n' +
              '<b>Ссылка для подключения:</b>\n<blockquote><code>' + server.link(data[0]) + '</code></blockquote>' +'\n\n' + server.print_stat(data[0]))
    await call.message.edit_media(InputMediaPhoto(media=FSInputFile(path=MAIN_PHOTO_PATH), caption=answer),
                                  reply_markup=profile_menu())

    await call.answer()


@profile_handlers.callback_query(F.data == 'профиль')
async def select_profile(call: CallbackQuery, bot: Bot):
    server.test_login()
    data = server.get_emails_user(call.from_user.id)


    if len(data) > 1:
        data_keyboard = {}
        for email in data:
            data_keyboard[email] = email
        data_keyboard['🔙 Назад'] = 'назад'
        print(data_keyboard)
        await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=keyboard_gen(data_keyboard))

    if len(data) == 1:
        text = (server.print_stat(data[0]) + '\n<b>Ссылка для подключения:</b>\n<blockquote><code>' + server.link(data[0]) +
                '</code></blockquote>\n\nЧтобы скопировать ссылку, просто нажмите на нее ☝️😎')
        await call.message.edit_media(InputMediaPhoto(media=FSInputFile(path=MAIN_PHOTO_PATH), caption=text),
                                      reply_markup=profile_menu())


    await call.answer()


@profile_handlers.callback_query(F.data == 'назад из профиля')
async def back_from_profile(call: CallbackQuery, bot: Bot):
    await call.message.edit_media(InputMediaPhoto(media=FSInputFile(path=MAIN_PHOTO_PATH), caption=TEXT_START),
                                  reply_markup=active_user_menu())
    await call.answer()


@profile_handlers.callback_query(F.data == 'продлить')
async def renew(call: CallbackQuery, bot: Bot):
    await call.answer()

@profile_handlers.callback_query(F.data == 'поделиться')
async def share(call: CallbackQuery, bot: Bot):
    await call.answer()