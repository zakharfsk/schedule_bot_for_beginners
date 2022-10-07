from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards import start_keyboad
from loader import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Вітання! Я бот, який допоможе тобі не забути про пари.",
        reply_markup=start_keyboad()
    )
