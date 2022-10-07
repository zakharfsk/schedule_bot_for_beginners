from datetime import datetime

from aiogram import types
from loguru import logger

from loader import dp
from models import Schedule, session


@logger.catch
def what_week_now() -> tuple[str, str]:
    nums = int(datetime.utcnow().isocalendar()[1])
    dt = datetime.now().strftime('%d.%m.%Y')
    if (nums % 2) == 0:
        return f"Сьогодні <code>{dt}</code> (поточний тиждень №{nums})  -  📌 <b>Знаменник</b>\n\n", 'Знаменник'
    if (nums % 2) != 0:
        return f"Сьогодні <code>{dt}</code> (поточний тиждень №{nums})  -  📌 <b>Чисельник</b>\n\n", 'Чисельник'


@dp.callback_query_handler(lambda c: c.data == "schedule")
@logger.catch
async def show_schedule(call: types.CallbackQuery):
    await call.answer()

    txt, tp_week = what_week_now()

    schedule = session.query(Schedule).filter(Schedule.type_week == tp_week).all()
    text = ""

    if schedule:
        text += txt
        for day in ["Понеділок", "Вівторок", "Середа", "Четвер", "П\'ятниця", "Субота"]:
            text += f"{day}:\n"
            for couple in schedule:
                if couple.day_week == day:
                    text += f"{couple.id}. " \
                            f"{couple.time_start_couple.strftime('%H:%M')} - " \
                            f"{couple.time_end_couple.strftime('%H:%M')} " \
                            f"{couple.name_couple} ({couple.teacher_couple} - {couple.audience_couple})\n"
            text += "\n"
    else:
        text = "Розклад пустий"

    await call.message.answer(text=text)
