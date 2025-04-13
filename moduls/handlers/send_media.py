from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaDocument
import moduls.utils.static_text as manuals


async def send_logs(message: Message, bot: Bot):
    log = r'/home/drojjin/.pm2/logs/tg-vyot-error.log'
    photo = "moduls/pictures/vpn.jpg"
    await message.delete()
    #media = [InputMediaPhoto(media=FSInputFile(path=photo)), InputMediaDocument(media=FSInputFile(path=log))]
    #await bot.edit_message_media(media=media, chat_id=message.chat.id)
    #await message.edit_media(InputMediaPhoto(media=FSInputFile(path=log), caption='sdzf'),
                                  #reply_markup=android_inline())

    # await message.edit_media(InputMediaDocument(media=log, caption=manuals.TEXT_START),
    #                               reply_markup=android_inline())
    await bot.send_document(message.chat.id, document=FSInputFile(path=log), caption='Логи')