import asyncio
from datetime import datetime

from aiogram.utils import executor
import aioschedule
from loguru import logger
from models import Schedule, session

from loader import dp

logger.add(
    "file.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {module}:{function}:{line} | {message}",
    level="DEBUG",
    enqueue=True,
    backtrace=True
)

ME = 618042376


async def check_schedule():
    logger.debug("Checking schedule")
    for schedule in session.query(Schedule).all():
        if schedule.time_start_couple == datetime.now().time():
            await dp.bot.send_message(ME, schedule.start_couple())
        elif schedule.time_end_couple == datetime.now().time():
            await dp.bot.send_message(ME, schedule.message)


async def scheduler():
    aioschedule.every(5).minutes.do(check_schedule)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(0.1)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == "__main__":
    from commands import *
    from callback_handlers import *
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
