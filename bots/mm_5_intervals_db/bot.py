import pandas as pd                             # Операции для Таблицы Данных
from time import sleep                          # Задаю Паузу между циклами выполнения Скрипта
import sqlite3 as sq                            # Библиотека  Работа с БД

import sys                                      # Помогает найти мои Модули
sys.path.append('.')
from data_bases.path_to_base import PATH        # Путь к БД
from api.request_xt import RequestXT            # Класс запрос по получению Уровней (Биржа XT)
from api.request_bitteam import RequestBitTeam  # Класс запрос по получению Объемов и выставления Ордеров (BitTeam)
# Конфигурационные Параметры
from bots.mm_5intervals.config import PAIR, INTERVALS, ACCOUNT, SECTION_DEPO, RATE_AMOUNT, STEP_PRICE, STEP_AMOUNT
# PAIR = 'del_usdt' # Торгуемая Пара
# INTERVALS = ['4h', '12h', '1d', '3d', '1w']
# SECTION_DEPO = 20 # Доля Торгуемого Капитала от Общего Депо в %
# ACCOUNT = {'name': 'Luchnik78', 'exchange': 'Bitteam'}
# RATE_AMOUNT = 1.5 # Коэфициент нарастания Объема
# STEP_PRICE = 6  # ШАГ Цен. Округлять до Знаков после точки
# STEP_AMOUNT = 6 # ШАГ Объемов. Округлять до Знаков после точки


class MM_5Levels(RequestXT, RequestBitTeam):

    def get_interval_high_low(self, interval):
        self.get_kline(symbol=PAIR, limit=2, interval=interval)
        self.high = max(float(self.data['result'][1]['h']), float(self.data['result'][0]['h']))
        self.low = min(float(self.data['result'][1]['l']), float(self.data['result'][0]['l']))
    def get_levels(self):
        df = pd.DataFrame(columns=['high', 'low'])
        for i in INTERVALS:
            self.get_interval_high_low(i)
            df.loc[i] = [self.high, self.low]
        self.levels = df
    def get_coins(self):
        self.coins = PAIR.upper().split('_')
    def get_quants(self):
        quant_0 = 1
        quant_1 = RATE_AMOUNT
        quant_2 = RATE_AMOUNT**2
        quant_3 = RATE_AMOUNT**3
        quant_4 = RATE_AMOUNT**4
        self.quants = (quant_0, quant_1, quant_2, quant_3, quant_4)
        self.sum_quant = quant_0 + quant_1 + quant_2 + quant_3 + quant_4
    def distribution_by_levels(self, index=0):
        quant_maunt = self.coin_amounts[self.coins[index]]/self.sum_quant
        maunts = []
        for i in self.quants:
            maunts.append(i * quant_maunt)
        self.levels[self.coins[index]] = maunts
    def get_amounts(self):
        if not self.auth:
            self.authorization(ACCOUNT)
        self.get_balance_compact()
        self.get_coins()

        coin_amounts = {}
        for coin in self.coins:
            if coin in self.balance.index:
                coin_amounts[coin] = float(self.balance['free'][coin])*SECTION_DEPO/100
        print(coin_amounts)
        self.coin_amounts = coin_amounts

        self.get_quants()
        for index in (0, 1):
            self.distribution_by_levels(index)
        print(self.levels)
    def create_my_orders(self):

        self.get_pair(pair=PAIR)
        pairId = self.data['result']['pair']['id']

        # Заглушка предварительно удаляю Вcе Ордера по Данной Паре
        # self.cancel_all_orders(pairId=pairId)

        # BUY ORDERS
        for i in self.levels.index:
            price = round(self.levels.at[i, 'low'] + 10**(-STEP_PRICE), STEP_PRICE) # (price in base coin (usdt))
            body = {'pairId': str(pairId),  # '44' farms_usdt, '24' del_usdt
                    'side': 'buy',  # "buy", "sell"
                    'type': 'limit',
                    'amount': round(self.levels.at[i, self.coins[1]] / price, STEP_AMOUNT), # (value in coin1 (del))
                    'price': price # (price in base coin (usdt))
                    }
            print(f'BUY Limit {PAIR}: {body}')
            self.create_order(body=body)
            if self.status == 200:
                insert_order_sql(self.data["result"]["id"], body)
        # SELL ORDERS
        for i in self.levels.index:
            price = round(self.levels.at[i, 'high'] - 10**(-STEP_PRICE), STEP_PRICE) #
            body = {'pairId': str(pairId),  # '44' farms_usdt, '24' del_usdt
                    'side': 'sell',  # "buy", "sell"
                    'type': 'limit',
                    'amount': round((self.levels.at[i, self.coins[0]]), STEP_AMOUNT), # (value in coin1 (del))
                    'price': price  # # (price in base coin (usdt))
                    }
            print(f'SELL Limit {PAIR}: {body}')
            self.create_order(body=body)
            if self.status == 200:
                insert_order_sql(self.data["result"]["id"], body)
def is_run_bot():
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("SELECT state FROM bot_mm_5_intervals_db ORDER BY rowid DESC")
        return bool(curs.fetchone()[0])

def insert_order_sql(id, body: dict):
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("INSERT INTO orders VALUES(?, (SELECT name FROM pairs WHERE id=?), ?, ?, ?, ?)",
                     (id, body['pairId'], body['side'], body['type'], body['amount'], body['price']))

def get_pairId_sql(pair):
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("SELECT id FROM pairs WHERE name LIKE ?", (pair,))
        return curs.fetchone()[0]

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

# --- RUN_BOT ----------------------------------------------------------------------------
while is_run_bot():
    strategy = MM_5Levels()         # Создаю Объект Стратегию
    strategy.authorization(ACCOUNT) # Авторизируюсь

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

    strategy.get_levels()           # Определяю Уровни на которых буду ставить Ордера на Пару
    strategy.get_amounts()          # Определяю Объемы (Размеры) Ордеров по Паре
    strategy.create_my_orders()     # Выставляю Ордера (предварительно удаляю все Активные Ордера по Паре)
    sleep(2*60*60) # Перерасчет Каждые 2 часа

# --- END RUN_BOT ----------------------------------------------------------------------------

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    pass
    # strategy = MM_5Levels()         # Создаю Объект Стратегию
    # strategy.authorization(ACCOUNT) # Авторизируюсь
    #
    # # Удаляю Все СВОИ Активные Ордера по этой паре
    # active_orders = get_my_orderId(PAIR)
    # print(active_orders)
    # for order in active_orders:
    #     strategy.cancel_order(order)
    # strategy.get_orders_of_user(limit=1000)
    # data_orders = strategy.data['result']['orders']
    # orders_in_books = []
    # for my_order in data_orders:
    #     orders_in_books.append(str(my_order['id']))
    # update_my_orders_sql(PAIR, orders_in_books)
    #
    # strategy.get_levels()           # Определяю Уровни на которых буду ставить Ордера на Пару
    # strategy.get_amounts()          # Определяю Объемы (Размеры) Ордеров по Паре
    # strategy.create_my_orders()     # Выставляю Ордера (предварительно удаляю все Активные Ордера по Паре)


if __name__ == '__main__':
    main()
