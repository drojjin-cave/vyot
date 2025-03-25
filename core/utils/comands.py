from aiogram import Bot
from aiogram.types import Message
from aiogram.types import BotCommand, BotCommandScopeDefault
from core.settings import settings


async def set_commands(bot: Bot):
    user_commands = [
            BotCommand(
                command="start",
                description='Начало работы'
            ),
        ]

    admin_commands = [
            BotCommand(
                command="start",
                description='Начало работы'
            ),
            BotCommand(
                command="logs",
                description='Логи'
            )
        ]

    await bot.set_my_commands(admin_commands, scope=BotCommandScopeDefault())


