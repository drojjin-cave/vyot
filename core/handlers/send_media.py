from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaDocument
import core.utils.manuals as manuals
from core.keyboards.reply import android_inline, back_in_menu_inline

async def send_logs(message: Message, bot: Bot):
    log = r'/home/drojjin/.pm2/logs/tg-vyot-error.log'
    photo = "core/pictures/vpn.jpg"
    await message.delete()
    #media = [InputMediaPhoto(media=FSInputFile(path=photo)), InputMediaDocument(media=FSInputFile(path=log))]
    #await bot.edit_message_media(media=media, chat_id=message.chat.id)
    #await message.edit_media(InputMediaPhoto(media=FSInputFile(path=log), caption='sdzf'),
                                  #reply_markup=android_inline())

    # await message.edit_media(InputMediaDocument(media=log, caption=manuals.TEXT_START),
    #                               reply_markup=android_inline())
    await bot.send_document(message.chat.id, document=FSInputFile(path=log), caption='Логи')