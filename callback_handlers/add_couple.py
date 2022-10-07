from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import time_start_keyboard, time_end_keyboard, start_keyboad, days_keyboard, type_week_keyboard
from loader import dp
from models import Schedule, session
from states import AddCouple


@dp.callback_query_handler(text="add_couple", state="*")
async def add_couple(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("Виберіть день тижня", reply_markup=days_keyboard())
    await AddCouple.day_week.set()


@dp.callback_query_handler(lambda c: c.data.startswith("day"), state=AddCouple.day_week)
async def add_day_week(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer("Введіть назву пари")
    await state.update_data(day_week=call.data.split("*")[1])
    await AddCouple.name.set()


@dp.message_handler(state=AddCouple.name)
async def add_couple_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введіть опис пари")
    await AddCouple.next()


@dp.message_handler(state=AddCouple.description)
async def add_couple_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer(
        "Виберіть час початку пари",
        reply_markup=time_start_keyboard()
    )
    await AddCouple.next()


@dp.callback_query_handler(lambda c: c.data.startswith('time_start'), state=AddCouple.time_start)
async def add_couple_time_start(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(time_start=datetime.strptime(call.data.split('*')[1], '%H:%M').time())
    await call.message.answer(
        "Виберіть час закінчення пари",
        reply_markup=time_end_keyboard()
    )
    await AddCouple.next()


@dp.callback_query_handler(lambda c: c.data.startswith('time_end'), state=AddCouple.time_end)
async def add_couple_time_end(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(time_end=datetime.strptime(call.data.split('*')[1], '%H:%M').time())
    await call.message.answer("Введіть викладача")
    await AddCouple.next()


@dp.message_handler(state=AddCouple.teacher)
async def add_couple_teacher(message: types.Message, state: FSMContext):
    await state.update_data(teacher=message.text)
    await message.answer("Введіть аудиторію")
    await AddCouple.next()


@dp.message_handler(state=AddCouple.audience)
async def add_couple_audience(message: types.Message, state: FSMContext):
    await state.update_data(audience=message.text)
    await message.answer(
        "Введіть тип неділі",
        reply_markup=type_week_keyboard()
    )
    await AddCouple.next()


@dp.callback_query_handler(lambda c: c.data.startswith('type_week'), state=AddCouple.type_week)
async def add_couple_type_week(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(type_week=call.data.split('*')[1])

    data = await state.get_data()
    session.add(
        Schedule(
            day_week=data["day_week"],
            name_couple=data['name'],
            description_couple=data['description'],
            time_start_couple=data['time_start'],
            time_end_couple=data['time_end'],
            teacher_couple=data['teacher'],
            audience_couple=data['audience'],
            type_week=data['type_week'],
        )
    )
    session.commit()

    await call.message.answer(
        "Пара успішно була додана",
        reply_markup=start_keyboad()
    )

    await state.finish()
