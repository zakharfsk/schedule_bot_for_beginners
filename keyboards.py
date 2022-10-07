from aiogram import types


def start_keyboad() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[
        types.InlineKeyboardButton(
            text="Переглянути розклад",
            callback_data="schedule",
        )
    ])
    keyboard.row(*[
        types.InlineKeyboardButton(
            text="Додати пару",
            callback_data="add_couple",
        ),
        types.InlineKeyboardButton(
            text="Видалити пару",
            callback_data="delete_couple",
        ),
        types.InlineKeyboardButton(
            text="Редагувати пару",
            callback_data="edit_couple",
        ),
    ])

    return keyboard


def time_start_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[
        types.InlineKeyboardButton(
            text="8:00",
            callback_data="time_start*8:00",
        ),
        types.InlineKeyboardButton(
            text="9:35",
            callback_data="time_start*9:35",
        ),
        types.InlineKeyboardButton(
            text="11:10",
            callback_data="time_start*11:10",
        ),
        types.InlineKeyboardButton(
            text="13:00",
            callback_data="time_start*13:00",
        ),
        types.InlineKeyboardButton(
            text="14:35",
            callback_data="time_start*14:35",
        ),
        types.InlineKeyboardButton(
            text="16:10",
            callback_data="time_start*16:10",
        ),
        types.InlineKeyboardButton(
            text="17:45",
            callback_data="time_start*17:45",
        ),
        types.InlineKeyboardButton(
            text="19:20",
            callback_data="time_start*19:20",
        ),
    ])

    return keyboard


def time_end_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[
        types.InlineKeyboardButton(
            text="9:20",
            callback_data="time_end*9:20",
        ),
        types.InlineKeyboardButton(
            text="10:55",
            callback_data="time_end*10:55",
        ),
        types.InlineKeyboardButton(
            text="12:30",
            callback_data="time_end*12:30",
        ),
        types.InlineKeyboardButton(
            text="14:20",
            callback_data="time_end*14:20",
        ),
        types.InlineKeyboardButton(
            text="15:55",
            callback_data="time_end*15:55",
        ),
        types.InlineKeyboardButton(
            text="17:30",
            callback_data="time_end*17:30",
        ),
        types.InlineKeyboardButton(
            text="19:05",
            callback_data="time_end*19:05",
        ),
        types.InlineKeyboardButton(
            text="20:40",
            callback_data="time_end*20:40",
        ),
    ])

    return keyboard


def days_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[
        types.InlineKeyboardButton(
            text="Понеділок",
            callback_data="day*Понеділок",
        ),
        types.InlineKeyboardButton(
            text="Вівторок",
            callback_data="day*Вівторок",
        ),
        types.InlineKeyboardButton(
            text="Середа",
            callback_data="day*Середа",
        ),
        types.InlineKeyboardButton(
            text="Четвер",
            callback_data="day*Четвер",
        ),
        types.InlineKeyboardButton(
            text="П'ятниця",
            callback_data="day*П\'ятниця",
        ),
        types.InlineKeyboardButton(
            text="Субота",
            callback_data="day*Субота",
        ),
    ])

    return keyboard


def type_week_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[
        types.InlineKeyboardButton(
            text="Знаменник",
            callback_data="type_week*Знаменник",
        ),
        types.InlineKeyboardButton(
            text="Чисельник",
            callback_data="type_week*Чисельник",
        )
    ])

    return keyboard


def edit_schedule_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    keyboard.add(
        types.KeyboardButton('Назву пари'),
        types.KeyboardButton('Опис пари'),
        types.KeyboardButton('Час початку'),
        types.KeyboardButton('Час закінчення'),
        types.KeyboardButton('Викладача'),
        types.KeyboardButton('Аудиторію'),
        types.KeyboardButton('День тижня'),
        types.KeyboardButton('Тип пари'),
    )

    return keyboard
