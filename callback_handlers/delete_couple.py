from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from models import Schedule, session
from states import DeleteCouple


@dp.callback_query_handler(lambda c: c.data == 'delete_couple', state='*')
async def delete_couple(call: types.CallbackQuery):
    await call.answer()

    schedules = session.query(Schedule).all()
    text = 'Виберіть номер пари, яку хочете видалити:\n\n'

    if schedules:
        for schedule in schedules:
            text += f"{schedule.id}. {schedule.name_couple} ({schedule.type_week})\n"

    await call.message.answer(text)

    await DeleteCouple.get_number_couple.set()


@dp.message_handler(state=DeleteCouple.get_number_couple)
async def get_number_couple(message: types.Message, state: FSMContext):
    try:
        session.query(Schedule).filter(Schedule.id == int(message.text)).delete()

        await message.answer('Пара успішно видалена!')
        await state.finish()
    except ValueError:
        await message.answer('Введіть номер пари!')
