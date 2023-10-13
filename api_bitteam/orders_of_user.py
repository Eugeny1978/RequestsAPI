import requests                         # библиотека для создания и обработки запросов
from auth import basic_auth             # Аутентификация
from constans import BASE_URL           # Базовый URL
from common_methods import write_data   # запись информации в файлы
from create_order import create_order   # Предварительно создам ордера
def get_orders_of_user(type='active', limit=10, offset=0, order='', where=''):
    """
    type= 'history', 'active', 'closed', 'cancelled', 'all'
    offset=х - смещение: не покажет первые Х ордеров
    {{baseUrl}}/trade/api/ccxt/ordersOfUser?limit=10&offset=0&type=active&order=<string>&where=<string>
    """
    # Необязательные Параметры
    if limit == 10:
        url_limit = ''
    else:
        url_limit = f'limit={limit}'

    if offset == 0:
        url_offset = ''
    else:
        url_offset = f'&offset={offset}'

    if order == '':
        url_order = ''
    else:
        url_order = f'&order={order}'

    if where == '':
        url_where = ''
    else:
        url_where = f'&where={where}'

    end_point = f'{BASE_URL}/ccxt/ordersOfUser?type={type}' + url_limit + url_offset + url_order + url_where
    responce = requests.get(url=end_point, auth=basic_auth)

    data = responce.json()
    name_file = f'orders_of_user'
    write_data(data, name_file)

    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    body_order1 = {'pairId': '24',  # del_usdt
                  'side': "buy",
                  'type': "limit",
                  'amount': '1000',
                  'price': '0.0165' }
    body_order2 = {'pairId': '44',  # farms_usdt
                   'side': "buy",
                   'type': "limit",
                   'amount': '500',
                   'price': '0.070' }
    create_order(body_order1)
    create_order(body_order2)

    data = get_orders_of_user()
    if data['ok']:
        print('Получил список Ордеров (см. файл json')
    else:
        print('Что-то пошло не так...')

if __name__ == '__main__':
    main()