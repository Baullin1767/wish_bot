from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from keyboards import wish_kb
from random import choice
from data_base import used_db, wish_db

async def get_rand_wish(wishes: dict):
    current_wish = choice(list(wishes.values()))
    return current_wish
    
    
async def get_wish(user_id):
    wishes = await wish_db.get_wishes_dict()
    done_wishes = await used_db.get_done_wish_list(user_id)
    new_wishes = {}

    for key, value in wishes.items():
        if value[0] != str(user_id) and done_wishes == None:
            new_wishes[key] = value
        elif value[0] != str(user_id) and value[1] not in done_wishes:
            new_wishes[key] = value
    
    return new_wishes

    

async def start_wish(message: types.Message, state: FSMContext):
    await message.answer('Начать выполнять желания?', reply_markup=wish_kb.yes_button)
    wishes = await get_wish(message.from_user.id)

    try:
        current_wish = choice(list(wishes.values()))
        await state.set_state('wishing')
        await state.update_data(wishes=wishes, current_wish=current_wish)
    except:
        await message.answer('Пока нет новых желаний')
        await state.reset_state()

    


async def send_wish(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    data = await state.get_data(call.from_user.id)
    wishes = data['wishes']
    current_wish = data['current_wish']

    if callback_data.get('done') == 'True':
            await used_db.add_done_wish(call)
            wishes = await get_wish(call.from_user.id)
    
    try:
        current_wish = choice(list(wishes.values()))
        await call.message.edit_text(f'Желание: {current_wish[1]}')
        await call.message.edit_reply_markup(wish_kb.wish_keybourd)
        await state.update_data(wishes=wishes, current_wish=current_wish)
    except:
        await call.message.edit_text('Пока нет новых желаний')
        await state.reset_state()

async def exit(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text('Выполнение желаний завершено')
    await state.reset_state()




def register_hendlers_wish(dp : Dispatcher):
    dp.register_message_handler(start_wish, commands=['wish'])
    dp.register_callback_query_handler(send_wish, wish_kb.callback_data_wish.filter(), state='wishing')
    dp.register_callback_query_handler(exit, wish_kb.exit_back_callback.filter(), state="*")