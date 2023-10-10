import requests                         # библиотека для создания и обработки запросов
import json                             # библиотека для обработки данных json
from config import BASE_URL, basic_auth # конфигурационные данные
from config import write_json_file      # запись информации в файлы
from time import sleep                  # пауза

def create_order(pairId, side, type, amount, price):
    """
    pairId: str # '44' farms_usdt
    side: str # buy, sell
    type: str # limit, market
    amount: str # '330' (value in coin1 (farms))
    price: str # '0.04' (price in base coin (usdt))
    """
    end_point = f'{BASE_URL}/ccxt/ordercreate'
    body = {'pairId': pairId,
            'side': side,
            'type': type,
            'amount': amount,
            'price': price }

    responce = requests.post(url=end_point, auth=basic_auth, data=body) # headers=headers, headers = {'user-agent': 'my-app/0.0.1'}
    data = responce.json()
    # name_file = f'create_order_{pairId[0]}_{side[0]}_{type[0]}_{amount[0]}_{price}'
    name_file = f'create_order_{data["result"]["pair"]}_{side}_{type}_{amount}_{price}'
    write_json_file(data, name_file)

    if data['ok']:
        print(f'Ордер Создан. ID: {data["result"]["id"]}')
    else:
        print('Что-то пошло не так...')

    return data

def get_order(id_order):
    end_point = f'{BASE_URL}/ccxt/order/{id_order}'
    responce = requests.get(url=end_point, auth=basic_auth)
    data = responce.json()
    name_file = f'get_order_{id_order}'
    write_json_file(data, name_file)
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
    body_order= ['44', 'buy', 'limit', '333', '0.03']
    data = create_order(body_order[0], body_order[1], body_order[2], body_order[3], body_order[4])
    id_order = data["result"]["id"]
    sleep(2)
    get_order(id_order)
    sleep(20)
    if data["ok"]:
        cancel_order(id_order)


if __name__ == '__main__':
    main()