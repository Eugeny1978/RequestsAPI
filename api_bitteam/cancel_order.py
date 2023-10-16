import requests                                     # Библиотека для создания и обработки запросов
from time import sleep                              # Пауза
from api_bitteam.auth import basic_auth             # Аутентификация
from api_bitteam.constants import BASE_URL          # Базовый URL
from api_bitteam.create_order import create_order   # Для отработки предварительно создам ордер
from common.methods import write_data               # Запись информации в файлы

def cancel_order(id_order: str, dump_json=False):
    """
    id_order = data['result']['id'] # create_order(body)
    """
    end_point = f'{BASE_URL}/ccxt/cancelorder'
    body = {"id": id_order}
    responce = requests.post(url=end_point, auth=basic_auth, data=body)
    data = responce.json()
    name_file = f'cancel_order_{id_order}'
    write_data(data, name_file, dump_json)

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
                  'amount': '300',
                  'price': '0.015'
                  }
    data = create_order(body_order, True)
    sleep(10)
    cancel_order(data['result']['id'], True)

if __name__ == '__main__':
    main()