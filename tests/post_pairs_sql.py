import requests                                 # Библиотека для создания и обработки запросов
from api.request import Request                 # Базовый Класс
import pandas as pd                             # Преобразовать Словари в Таблицы
import sqlite3 as sq                            # Библиотека  Работа с БД
from data_bases.path_to_base import PATH        # Путь к БД
from api.request_bitteam import RequestBitTeam

class XXX(RequestBitTeam):
    def post_pairs_sql(self):
        self.info_pairs()
        with sq.connect(PATH) as connect_db:
            # connect_db.row_factory = sq.Row  # Если хотим строки записей в виде dict {}. По умолчанию - кортежи turple ()
            cursor_db = connect_db.cursor()

            cursor_db.execute("""CREATE TABLE IF NOT EXISTS pairs
            (id INTEGER PRIMARY KEY, name TEXT, baseStep INTEGER, quoteStep INTEGER)""")

            cursor_db.execute("""DELETE FROM pairs""")

            for pair in self.data['result']['pairs']:
                cursor_db.execute("""
                INSERT INTO pairs (id, name, baseStep, quoteStep) 
                VALUES (:Id, :Name, :BaseStep, :QuoteStep)
                 """, {'Id': pair['id'], 'Name': pair['name'], 'BaseStep': pair['baseStep'], 'QuoteStep': pair['quoteStep']})

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    # xxx = XXX()
    # xxx.post_pairs_sql()

    PATH = "F:/! PYTON/PyCharm/RequestsAPI/data_bases/base.db"
    with sq.connect(PATH) as connect_db:
        cursor_db = connect_db.cursor()
        cursor_db.execute("""SELECT name FROM pairs""")
        pairs = []
        for pair in cursor_db:
            pairs.append(pair[0])
    print(pairs)

if __name__ == '__main__':
    main()

