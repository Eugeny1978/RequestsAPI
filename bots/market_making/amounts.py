import pandas as pd                             # Операции для Таблицы Данных
from api_xt.kline import get_kline              # API Запрос Исторические Свечи
import bots.market_making.config as config      # Настраиваемые Параметры Бота
from api_bitteam.pair import get_pair           # Информация по Торгуемой Паре
from api_bitteam.balance import get_balance     # Текущий Баланс

account = 'Account_01'

coins = config.PAIR.upper().split('_')
print(coins)
api_keys = config.get_api_keys(account)
balance_data = get_balance()

# total_amount = config.SECTION_DEPO *
#
# data = get_pair(config.PAIR)
