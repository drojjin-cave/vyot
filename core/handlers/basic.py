from aiogram import Bot
from aiogram.types import Message, FSInputFile
from core.keyboards.reply import start_keyboard, user_menu_inline, admin_menu_inline, active_user_menu
from core.utils.dbconnect import get_user, check_db
import core.utils.manuals as manuals
from core.settings import settings
from core.utils.x3_UI import X3_UI

server = X3_UI()
start_message_id = []
async def get_start(message: Message, bot: Bot):
    photo = "core/pictures/vpn.jpg"

    check = server.check_user(message.from_user.id)
    if not check:
        await bot.send_photo(message.from_user.id, photo=FSInputFile(path=photo), caption=manuals.TEXT_START, reply_markup=user_menu_inline())
    else:
        mymessage = await bot.send_photo(message.from_user.id, photo=FSInputFile(path=photo), caption=manuals.TEXT_START, reply_markup=active_user_menu())
        start_message_id.append(mymessage.message_id)


