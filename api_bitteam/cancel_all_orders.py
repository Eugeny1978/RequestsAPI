import requests                             # библиотека для создания и обработки запросов
from auth import basic_auth                 # Аутентификация
from constants import BASE_URL              # Базовый URL, Папка Логов
from common.methods import write_data       # запись информации в файлы
from create_order import create_order       # Для отработки предварительно создам ордер
from time import sleep                      # пауза

def cancel_all_orders(pairId=0):
    """
    pairId 1-100 - по конкретной паре || 0 - all pairs
    """
    end_point = f'{BASE_URL}/ccxt/cancel-all-order'
    body = {"pairId": pairId }
    responce = requests.post(url=end_point, auth=basic_auth, data=body)
    data = responce.json()
    name_file = f'cancel_all_orders_{pairId}'
    write_data(data, name_file)


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    body_order1 = {'pairId': '24',  # del_usdt
                  'side': "buy",
                  'type': "limit",
                  'amount': '1000',
                  'price': '0.017'
                  }
    body_order2 = {'pairId': '24',  # del_usdt
                   'side': "buy",
                   'type': "limit",
                   'amount': '500',
                   'price': '0.0165'
                   }
    body_order3 = {'pairId': '44',  # farms_usdt
                   'side': "buy",
                   'type': "limit",
                   'amount': '300',
                   'price': '0.04'
                   }

    # create_order(body_order1)
    # create_order(body_order1)
    # create_order(body_order1)
    # sleep(30)
    # cancel_all_orders(44)
    cancel_all_orders()

if __name__ == '__main__':
    main()