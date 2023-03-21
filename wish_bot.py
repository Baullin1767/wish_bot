from aiogram.utils import executor
from create_bot import dp
from mic.set_bot_command import set_default_commands
from data_base import wish_db, used_db


async def on_startup(_):
    print('Бот онлайн')
    await set_default_commands(dp)
    await wish_db.wish_dp_start()
    await used_db.start_user_db()


from handlers import add_wish, start, wish

add_wish.register_hendlers_add_wish(dp)
start.register_hendlers_start(dp)
wish.register_hendlers_wish(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)