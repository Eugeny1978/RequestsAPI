import streamlit as st                          # Библиотека Компоновщик Страниц Интерфейся
import sqlite3 as sq                            # Библиотека  Работа с БД
from data_bases.path_to_base import PATH        # Путь к БД
import pandas as pd                             # Преобразовать Словари в Таблицы


with sq.connect(PATH) as connect:
    connect.row_factory = sq.Row  # Если хотим строки записей в виде dict {}. По умолчанию - кортежи turple ()
    curs = connect.cursor()

    curs.execute("""SELECT name FROM pairs ORDER BY name""")
    pairs = []
    for pair in curs:
        pairs.append(pair['name'])

    curs.execute("""SELECT * FROM trade_api ORDER BY name""")
    accounts = pd.DataFrame(columns=['name', 'exchange', 'public_key', 'secret_key'])
    for account in curs:
        accounts.loc[len(accounts.index)]= [account['name'], account['exchange'], account['public_key'], account['secret_key']]

    print(accounts.loc[:, ('name', 'exchange')])