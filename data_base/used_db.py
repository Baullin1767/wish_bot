import sqlite3 as sq
from aiogram import types

#Подклчение базы данных
async def start_user_db():
    global base, cur
    base = sq.connect('user_db.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT, done_wish TEXT PRIMARY KEY)')
    base.commit()

#Добавление завершённого желения
async def add_done_wish(call: types.CallbackQuery):
    user_id = call.from_user.id
    text_wish = call.message.text.split('Желание: ')
    text_wish = text_wish[1]

    cur.execute('INSERT INTO users VALUES (?, ?)', (user_id, text_wish,))
    base.commit()

#Получение завершённых заданий
async def get_done_wish_list(user_id):
    with base:
        result = cur.execute("SELECT * FROM users").fetchall()
        user_base = {}
        
        for row in result:
            if row[0] in user_base:
                user_base[row[0]].append(row[1])
            else:
                user_base[row[0]] = [row[1]]
        try:        
            return user_base[str(user_id)]
        except:
            None