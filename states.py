from aiogram.dispatcher.filters.state import State, StatesGroup


class AddCouple(StatesGroup):
    day_week = State()
    name = State()
    description = State()
    time_start = State()
    time_end = State()
    teacher = State()
    audience = State()
    type_week = State()


class DeleteCouple(StatesGroup):
    get_number_couple = State()


class EditCouple(StatesGroup):
    get_number_couple = State()
    type_edit = State()
    edit = State()
