import sys
sys.path.append('.')
from api.request_bitteam import RequestBitTeam  # Класс запросы (BitTeam)
from bots.mm_5intervals.config_old import PAIR, ACCOUNT # Конфигурационные Параметры

strategy = RequestBitTeam()         # Создаю Объект Стратегию
strategy.authorization(ACCOUNT) # Авторизируюсь

# Удаляю Все Активные Ордера по этой паре
strategy.get_pair(pair=PAIR)
pairId = strategy.data['result']['pair']['id']
strategy.cancel_all_orders(pairId=pairId)


# # ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
# def main():
#     pass
#
# if __name__ == '__main__':
#     main()
