from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from data_base import wish_db



async def start_add_wish(message: types.Message, state: FSMContext):
    await message.answer('Пришлите желание, которое хотите добавить:')
    await state.set_state('add_wish')


async def add_new_with_in_db(message: types.Message, state: FSMContext):
    await wish_db.add_new_wish(message)
    await message.answer('Желание добавлено')
    await state.reset_state()



def register_hendlers_add_wish(dp : Dispatcher):
    dp.register_message_handler(start_add_wish, commands=['add_wish'])
    dp.register_message_handler(add_new_with_in_db, state='add_wish')