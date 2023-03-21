import sqlite3 as sq
from aiogram import types

#Подклчение базы данных
async def wish_dp_start():
    global base, cur
    base = sq.connect('wish_db.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS wish(user_id TEXT, wish TEXT PRIMARY KEY)')
    base.commit()


#Добавление нового желения
async def add_new_wish(message: types.Message):
    user_id = message.from_user.id
    text_wish = message.text

    cur.execute('INSERT INTO wish VALUES (?, ?)', (user_id, text_wish,))
    base.commit()

#Получение списка желений
async def get_wishes_dict():
    with base:
        result = cur.execute("SELECT * FROM wish").fetchall()
        wishes_dict = {}
        
        i=1
        for row in result:
            wishes_dict.update({i: (row[0], row[1])})
            i+=1
        return wishes_dict
