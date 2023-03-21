from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback_data_wish = CallbackData('next', 'done')

exit_back_callback = CallbackData('exit', 'reset_state')

yes_button = InlineKeyboardMarkup()\
    .add(
    InlineKeyboardButton(
        text='Да!', callback_data=callback_data_wish.new(
            done='False'
        )
    )
).add(
    InlineKeyboardButton(
        text='Нет!', callback_data=exit_back_callback.new(reset_state = 'True')
    )
)


wish_keybourd = InlineKeyboardMarkup()\
.add(
    InlineKeyboardButton(
        text='Выполнил', 
        callback_data=callback_data_wish.new(done='True')
    )
).add(
    InlineKeyboardButton(
        text='Выполню потом',
        callback_data=callback_data_wish.new(done='False')
    )
).add(
    InlineKeyboardButton(
        text='Уже выполнял',
        callback_data=callback_data_wish.new(done='True')
    )
).add(InlineKeyboardButton(
        text='Выход', 
        callback_data=exit_back_callback.new(reset_state = 'True')
    ))