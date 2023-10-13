import requests                         # библиотека для создания и обработки запросов
from auth import basic_auth             # Аутентификация
from constans import BASE_URL           # Базовый URL
from common_methods import write_data   # запись информации в файлы

def get_trades_of_user(limit=10, offset=0, order='', pairId=0):
    """
    offset=х - смещение: не покажет первые Х сделок
    pairId=0 - все пары # 24 - del_usdt
    ccxt/tradesOfUser?limit=10&offset=0&order=<string>&pairId=<integer>
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

    if pairId == 0:
        url_pairId = ''
    else:
        url_pairId = f'&pairId={pairId}'

    end_point = f'{BASE_URL}/ccxt/tradesOfUser?' + url_limit + url_offset + url_order + url_pairId
    responce = requests.get(url=end_point, auth=basic_auth)

    data = responce.json()
    name_file = f'trades_of_user'
    write_data(data, name_file)

    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    # data = get_trades_of_user(limit=20)
    # data = get_trades_of_user(limit=5, offset=3, pairId=24)
    data = get_trades_of_user()
    if data['ok']:
        print('Получил список Сделок (см. файл json')
    else:
        print('Что-то пошло не так...')

if __name__ == '__main__':
    main()