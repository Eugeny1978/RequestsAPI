import requests                                     # Библиотека для создания и обработки запросов
from time import sleep                              # Пауза
from api_bitteam.auth import basic_auth             # Аутентификация
from api_bitteam.constants import BASE_URL          # Базовый URL
from api_bitteam.create_order import create_order   # Для отработки предварительно создам ордер
from common.methods import write_data               # Запись информации в файлы

def get_order(order_id, dump_json=False):
    """
    """
    end_point = f'{BASE_URL}/ccxt/order/{order_id}'
    responce = requests.get(url=end_point, auth=basic_auth)
    data = responce.json()
    name_file = f'get_order_{order_id}'
    write_data(data, name_file, dump_json)
    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    body_order = {'pairId': '24',  # del_usdt
                  'side': "buy",
                  'type': "limit",
                  'amount': '450',
                  'price': '0.015'
                  }
    data = create_order(body_order, True)
    if data['ok']:
        order_id = data["result"]["id"]
        print(f'Ордер Создан. ID: {order_id}')
        sleep(10)
        get_data = get_order(order_id)
        print(get_data)


if __name__ == '__main__':
    main()