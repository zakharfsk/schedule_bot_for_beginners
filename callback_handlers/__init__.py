from loguru import logger

from callback_handlers import add_couple
from callback_handlers import delete_couple
from callback_handlers import edit_couple
from callback_handlers import show_schedule

logger.debug(f'Loaded {globals()["__name__"]}')
