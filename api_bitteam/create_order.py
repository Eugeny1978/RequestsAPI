import requests                             # библиотека для создания и обработки запросов
from auth import basic_auth                 # Аутентификация
from constants import BASE_URL              # Базовый URL, Папка Логов
from common.methods import write_data       # запись информации в файлы

def create_order(body):
    """
    body = {'pairId':   str, #  '44' farms_usdt, '24' del_usdt
            'side':     str, # "buy", "sell"
            'type':     str, # "limit", "market", ??? - "conditional" - отрабатывает но непончтна цена прикоторой ордер превпатится в лимитный
            'amount':   str, # '330' (value in coin1 (farms))
            'price':    str  # '0.04' (price in base coin (usdt))
            }
    """
    end_point = f'{BASE_URL}/ccxt/ordercreate'
    responce = requests.post(url=end_point, auth=basic_auth, data=body) # headers=headers, headers = {'user-agent': 'my-app/0.0.1'}

    data = responce.json()
    try:
        name_file = f'create_order_{data["result"]["pair"]}_{body["side"]}_{body["type"]}_{body["amount"]}_{body["price"]}_{data["result"]["id"]}'
        write_data(data, name_file)
    except Exception as error:
        print(error)

    return data


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    # body_order = {'pairId': '24', # del_usdt
    #             'side': "buy",
    #             'type': "limit",
    #             'amount': '1000',
    #             'price': '0.017'
    #             }
    # data = create_order(body_order)

    body_order = {'pairId': '24', # del_usdt
                'side': "buy",
                'type': "limit",
                'amount': '500',
                'price': '0.015'
                #"stopPrice": "0.0175"
                #'slippage': '100'
                }
    data = create_order(body_order)

    if data['ok']:
        print(f'Ордер Создан. ID: {data["result"]["id"]}')
    else:
        print('Что-то пошло не так...')


if __name__ == '__main__':
    main()