from aiogram import types, Dispatcher
from data_base import used_db, wish_db



async def command_start(message: types.Message):
    await message.answer('Воспользуйтесь меню, чтобы добавить или выполнить желание')




def register_hendlers_start(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])