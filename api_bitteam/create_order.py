import requests                             # Библиотека для создания и обработки запросов
from api_bitteam.auth import basic_auth     # Аутентификация
from api_bitteam.constants import BASE_URL  # Базовый URL
from common.methods import write_data       # Запись информации в файлы

def create_order(body, dump_json=False):
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
        write_data(data, name_file, dump_json)
    except Exception as error:
        print(error)

    return data


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    # body_order = {'pairId': '44', # farms_usdt. Необходимо продать 1996 шт. 2023/10/17 Торгов нет Ордера не выводятся в стакан
    #             'side': "sell",
    #             'type': "limit",
    #             'amount': '1996',
    #             'price': '0.53334'
    #             }
    # data = create_order(body_order, True)

    body_order = {'pairId': '24', # del_usdt
                'side': "sell",
                'type': "limit",
                'amount': '6.123456', # '6.12345678' 8 знаков после точки
                'price': '0.017991'   # '0.017991' 6 знаков после точки
                #"stopPrice": "0.0175"
                #'slippage': '100'
                }
    data = create_order(body_order, True)

    if data['ok']:
        print(f'Ордер Создан. ID: {data["result"]["id"]}')
    else:
        print('Что-то пошло не так...')


if __name__ == '__main__':
    main()