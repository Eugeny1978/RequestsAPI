import requests                         # библиотека для создания и обработки запросов
from auth import basic_auth             # Аутентификация
from constans import BASE_URL           # Базовый URL
from common_methods import write_data   # запись информации в файлы
from create_order import create_order   # Для отработки предварительно создам ордер
from time import sleep                  # пауза


def cancel_order(id_order: str):
    """
    id_order = data['result']['id'] # create_order(body)
    """
    end_point = f'{BASE_URL}/ccxt/cancelorder'
    body = {"id": id_order}
    responce = requests.post(url=end_point, auth=basic_auth, data=body)
    data = responce.json()
    name_file = f'cancel_order_{id_order}'
    write_data(data, name_file)

    if data['ok']:
        print(f'Ордер Удален. ID: {id_order}')
    else:
        print('Что-то пошло не так...')

    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    body_order = {'pairId': '24',  # del_usdt
                  'side': "buy",
                  'type': "limit",
                  'amount': '1000',
                  'price': '0.017'
                  }
    data = create_order(body_order)
    sleep(10)
    cancel_order(data['result']['id'])

if __name__ == '__main__':
    main()