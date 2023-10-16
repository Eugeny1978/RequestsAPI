import requests                             # Библиотека для создания и обработки запросов
from api_bitteam.auth import basic_auth     # Аутентификация
from api_bitteam.constants import BASE_URL  # Базовый URL
from common.methods import write_data       # Запись информации в файлы

def get_trades_of_user(limit=10, offset=0, order='', pairId=0, dump_json=False):
    """
    offset=х - смещение: не покажет первые Х сделок
    pairId=0 - все пары # 24 - del_usdt
    ccxt/tradesOfUser?limit=10&offset=0&order=<string>&pairId=<integer>
    """
    # Необязательные Параметры
    url_limit = '' if limit == 10 else f'limit={limit}'
    url_offset = '' if offset == 0 else f'&offset={offset}'
    url_order = '' if order == '' else f'&order={order}'
    url_pairId = '' if pairId == 0 else f'&pairId={pairId}'

    end_point = f'{BASE_URL}/ccxt/tradesOfUser?' + url_limit + url_offset + url_order + url_pairId
    responce = requests.get(url=end_point, auth=basic_auth)

    data = responce.json()
    name_file = f'trades_of_user'
    write_data(data, name_file, dump_json)

    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    # data = get_trades_of_user(limit=20)
    # data = get_trades_of_user(limit=5, offset=3, pairId=24)
    data = get_trades_of_user(dump_json=True)
    if data['ok']:
        print('Получил список Сделок (см. файл json')
    else:
        print('Что-то пошло не так...')

if __name__ == '__main__':
    main()