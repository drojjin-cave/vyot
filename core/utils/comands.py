from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault



async def set_commands(bot: Bot):
    user_commands = [
            BotCommand(
                command="start",
                description='Начало работы'
            ),
        ]

    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())


