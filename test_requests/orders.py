import requests                         # библиотека для создания и обработки запросов
import json                             # библиотека для обработки данных json
from config import BASE_URL, basic_auth # конфигурационные данные
from config import write_json_file      # запись информации в файлы
from time import sleep                  # пауза



def create_order():
    # {
    #   "pairId": "2",
    #   "side": "buy | sell",
    #   "type": "limit | market",
    #   "amount": "500 //quantity (eth)",
    #   "price": "153 //price (btc)"
    # }

    # headers = {'user-agent': 'my-app/0.0.1'}
    end_point = f'{BASE_URL}/ccxt/ordercreate'
    pairId = '44' # farms_usdt
    side = 'buy',
    type = 'limit',
    amount = '330',
    price = '0.03'

    body = {'pairId': pairId,
            'side': side,
            'type': type,
            'amount': amount,
            'price': price }

    responce = requests.post(url=end_point, auth=basic_auth, data=body) # headers=headers,
    data = responce.json()
    name_file = f'create_order_{pairId[0]}_{side[0]}_{type[0]}_{amount[0]}_{price}'
    write_json_file(data, name_file)

    if data['ok']:
        print(f'Ордер Создан. ID: {data["result"]["id"]}')
    else:
        print('Что-то пошло не так...')

    return data

def cancel_order(id_order):
    end_point = f'{BASE_URL}/ccxt/cancelorder'
    body = {"id": id_order}
    responce = requests.post(url=end_point, auth=basic_auth, data=body)
    data = responce.json()
    name_file = f'cancel_order_{id_order}'
    write_json_file(data, name_file)

    if data['ok']:
        print(f'Ордер Удален. ID: {id_order}')
    else:
        print('Что-то пошло не так...')

    return data


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    data = create_order()
    sleep(30)
    if data["ok"]:
        cancel_order(data["result"]["id"])


if __name__ == '__main__':
    main()