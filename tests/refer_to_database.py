import sqlite3 as sq                        # Библиотека для работы с БД
from data_bases.path_to_base import PATH

# Добиться результата:
# F:\\! PYTON\\PyCharm\\RequestsAPI\\data_bases\\base.db
# print(PATH)

with sq.connect(PATH) as connect_db:
    cursor_db = connect_db.cursor()
    cursor_db.execute("""
    CREATE TABLE IF NOT EXISTS trade_api (
    name TEXT UNIQUE,
    exchange TEXT,
    public_key TEXT UNIQUE,
    secret_key TEXT UNIQUE)
    """)

    cursor_db.execute("""SELECT * FROM trade_api""")
    rows = cursor_db.fetchall()
    print(rows, '\n')








