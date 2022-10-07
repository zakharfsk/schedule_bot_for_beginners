from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from loguru import logger

from keyboards import edit_schedule_keyboard
from loader import dp
from models import session, Schedule
from states import EditCouple


@dp.callback_query_handler(lambda c: c.data == 'edit_couple', state='*')
@logger.catch
async def edit_couple(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    schedules = session.query(Schedule).all()
    session.close()
    text = 'Виберіть номер пари, яку ви хочете змінити:\n\n'

    if schedules:
        for schedule in schedules:
            text += f"{schedule.id}. {schedule.name_couple} ({schedule.type_week})\n"
    else:
        text = 'Розклад пустий!'

    await call.message.answer(text)
    await EditCouple.get_number_couple.set()


@dp.message_handler(state=EditCouple.get_number_couple)
@logger.catch
async def get_number_couple(message: types.Message, state: FSMContext):
    try:
        number_couple = int(message.text)

        schedules = session.query(Schedule).filter(Schedule.id == number_couple).first()
        session.close()

        await message.answer(
            f'Назва: <code>{schedules.name_couple}</code>\n'
            f'Опис: <code>{schedules.description_couple}</code>\n'
            f'Час початку: <code>{schedules.time_start_couple.strftime("%H:%M")}</code>\n'
            f'Час закінчення: <code>{schedules.time_end_couple.strftime("%H:%M")}</code>\n'
            f'Викладач: <code>{schedules.teacher_couple}</code>\n'
            f'Аудиторія: <code>{schedules.audience_couple}</code>\n'
            f'Тип неділі: <code>{schedules.type_week}</code>\n',
        )

        await state.update_data(number_couple=number_couple)
        await message.answer(
            'Що саме ви хочете змінити?',
            reply_markup=edit_schedule_keyboard()
        )
        await EditCouple.next()

    except ValueError:
        await message.answer('Введіть номер пари, яку ви хочете змінити!')


@dp.message_handler(state=EditCouple.type_edit)
@logger.catch
async def type_edit(message: types.Message, state: FSMContext):
    if message.text in ['Назву пари', 'Опис пари', 'Час початку',
                        'Час закінчення', 'Викладача', 'Аудиторію', 'День тижня', 'Тип пари']:
        await state.update_data(type_edit=message.text)
        await message.answer('Введіть нове значення', reply_markup=types.ReplyKeyboardRemove())
        await EditCouple.next()
    else:
        await message.answer('Виберіть один з варіантів на клавіатурі')


@dp.message_handler(state=EditCouple.edit)
@logger.catch
async def edit(message: types.Message, state: FSMContext):
    data = await state.get_data()

    number_couple = data.get('number_couple')
    type_schedule_edit = data.get('type_edit')
    value = message.text

    schedule = session.query(Schedule).filter(Schedule.id == number_couple).first()

    match type_schedule_edit:
        case 'Назву пари':
            schedule.name_couple = value
        case 'Опис пари':
            schedule.description_couple = value
        case 'Час початку':
            schedule.time_start_couple = datetime.strptime(message.text, '%H:%M').time()
        case 'Час закінчення':
            schedule.time_end_couple = datetime.strptime(message.text, '%H:%M').time()
        case 'Викладача':
            schedule.teacher_couple = value
        case 'Аудиторію':
            schedule.audience_couple = value
        case 'День тижня':
            schedule.day_week = value
        case 'Тип пари':
            schedule.type_week = value

    session.commit()
    session.close()
    await message.answer('Ваш розклад було змінено')
    await state.finish()
