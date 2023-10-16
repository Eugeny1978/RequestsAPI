import requests                             # библиотека для создания и обработки запросов
from auth import basic_auth                 # Аутентификация
from constants import BASE_URL              # Базовый URL, Папка Логов
from common.methods import write_data       # запись информации в файлы
from create_order import create_order       # Для отработки предварительно создам ордер
from time import sleep                      # пауза

def get_order(order_id):
    """
    """
    end_point = f'{BASE_URL}/ccxt/order/{order_id}'
    responce = requests.get(url=end_point, auth=basic_auth)
    data = responce.json()
    name_file = f'get_order_{order_id}'
    write_data(data, name_file)
    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    body_order = {'pairId': '24',  # del_usdt
                  'side': "buy",
                  'type': "limit",
                  'amount': '450',
                  'price': '0.015'
                  }
    data = create_order(body_order)
    if data['ok']:
        order_id = data["result"]["id"]
        print(f'Ордер Создан. ID: {order_id}')
        sleep(10)
        get_data = get_order(order_id)
        print(get_data)


if __name__ == '__main__':
    main()