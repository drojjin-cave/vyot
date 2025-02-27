import aiosqlite
from aiogram.types import Message
import asyncio

message = Message


async def get_user(id_tg):
    conn = await aiosqlite.connect('../database.db')
    async with conn.cursor() as cur:
        try:
            await cur.execute(f"SELECT * FROM users WHERE id_tg={id_tg}")
            result = await cur.fetchone()
            return result
        except:
            return None


async def add_user(id_tg, name):
    conn = await aiosqlite.connect('../database.db')
    async with conn.cursor() as cur:
        try:
            await cur.execute(f"INSERT INTO users (id_tg, name) VALUES (?, ?)", (id_tg, name))
            await conn.commit()
            return True
        except:
            return None

