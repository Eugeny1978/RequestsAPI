import sqlite3 as sq                            # Библиотека  Работа с БД

import sys                                      # Помогает найти мои Модули
sys.path.append('.')
from api.request_bitteam import RequestBitTeam  # Класс запросы (BitTeam)
from bots.mm_5intervals.config_old import PAIR, ACCOUNT # Конфигурационные Параметры
from data_bases.path_to_base import PATH        # Путь к БД

def get_my_orderId(pair) -> list:
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("SELECT id FROM orders WHERE pair LIKE ?", (pair,))
        orders = []
        for select in curs:
            orders.append(select[0])
        return orders

def update_my_orders_sql(pair, orders_in_books):
    orders_in_table = get_my_orderId(pair)
    orders_for_del = []
    for order in orders_in_table:
        if order not in orders_in_books:
            orders_for_del.append(order)

    if len(orders_for_del) > 0:
        with sq.connect(PATH) as connect:
            curs = connect.cursor()
            id_str = ','.join(map(str, orders_for_del))
            curs.execute(f"DELETE FROM orders WHERE id IN ({id_str})")

# ------------------------------------------------------------------------------


strategy = RequestBitTeam()         # Создаю Объект Стратегию
strategy.authorization(ACCOUNT)     # Авторизируюсь

# Удаляю Все СВОИ Активные Ордера по этой паре
active_orders = get_my_orderId(PAIR)
print(active_orders)
for order in active_orders:
    strategy.cancel_order(order)
strategy.get_orders_of_user(limit=1000)
data_orders = strategy.data['result']['orders']
orders_in_books = []
for my_order in data_orders:
    orders_in_books.append(str(my_order['id']))
update_my_orders_sql(PAIR, orders_in_books)