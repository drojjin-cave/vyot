from aiogram import Bot
from aiogram.types import Message
from aiogram.types import BotCommand, BotCommandScopeDefault
from moduls.settings import settings

ADMINS_VPN = settings.bots.admins_vpn

user_commands = [
    BotCommand(
        command="start",
        description='Перезапустить бота'
    ),
]

admin_commands = [
    BotCommand(
        command="start",
        description='Перезапустить бота'
    ),
    BotCommand(
        command="logs",
        description='Логи'
    )
]


async def set_commands(bot: Bot, id):
    if id in ADMINS_VPN:
        await bot.set_my_commands(admin_commands, scope=BotCommandScopeDefault())
    else:
        await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())


