from aiogram import Bot
from aiogram.types import Message
from aiogram.types import BotCommand, BotCommandScopeDefault
from core.settings import settings


async def set_commands(bot: Bot):
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

    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())


