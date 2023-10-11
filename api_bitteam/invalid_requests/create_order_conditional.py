import requests                         # библиотека для создания и обработки запросов
from auth import basic_auth             # Аутентификация
from constans import BASE_URL           # Базовый URL
from common_methods import write_data   # запись информации в файлы

# С авторизацией Пользователя НЕ РАБОТАЕТ!

def create_order(body):
    """
    body = {'pairId':   int, #  44 - farms_usdt, 24 - del_usdt
            'side':     str, # "buy", "sell"
            'type':     str, # "limit", "market"
            'amount':   str, # '330' (value in coin1 (farms))
            'price':    str, # '0.04' (price in base coin (usdt))
            'slippage': int  # 100
            }
    """

    end_point = f'{BASE_URL}/order/conditional/create'
    responce = requests.post(url=end_point, auth=basic_auth, data=body) # headers=headers, headers = {'user-agent': 'my-app/0.0.1'}

    data = responce.json()

    name_file = f'create_order_{data["result"]["pair"]}_{body["side"]}_{body["type"]}_{body["amount"]}_{body["price"]}_{data["result"]["id"]}'
    write_data(data, name_file)

    return data


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    body_order = {'pairId': 24, # del_usdt
                'side': "buy",
                'type': "conditional",
                'amount': '1000',
                'price': '0.017',
                'slippage': 100
                }
    data = create_order(body_order)

    if data['ok']:
        print(f'Условный Ордер Создан. ID: {data["result"]["id"]}')
    else:
        print('Что-то пошло не так...')


if __name__ == '__main__':
    main()