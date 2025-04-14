from aiogram import Router, F, Bot
from aiogram.types import  CallbackQuery, InputMediaPhoto, FSInputFile

from moduls.keyboards.manual_keyboard import manual_keyboard, back_from_manuals_keyboard

from moduls.utils.static_text import *

manuals_handlers = Router(name=__name__)


@manuals_handlers.callback_query(F.data == 'инструкции')
async def select_manual(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=manual_keyboard())

    await call.answer()


@manuals_handlers.callback_query(F.data == 'андроид')
async def manual_android(call: CallbackQuery, bot: Bot):
    '''Инструкция андроид'''
    await call.message.edit_media(InputMediaPhoto(media=FSInputFile(path=ANDROID_PHOTO_PATH), caption=MANUAL_ANDROID),
                                  reply_markup=back_from_manuals_keyboard())

    await call.answer()


@manuals_handlers.callback_query(F.data == 'айфон')
async def manual_apple(call: CallbackQuery):
    '''Инструкция айфон'''
    await call.message.edit_media(InputMediaPhoto(media=FSInputFile(path=APPLE_PHOTO_PATH), caption=MANUAL_APPLE),
                                  reply_markup=back_from_manuals_keyboard())
    await call.answer()



@manuals_handlers.callback_query(F.data == 'назад_из_инструкций')
async def back_from_manuals(call: CallbackQuery):
    '''Назад из инструкций'''
    await call.message.edit_media(InputMediaPhoto(media=FSInputFile(path=MAIN_PHOTO_PATH), caption=TEXT_START), reply_markup=manual_keyboard())
    await call.answer()