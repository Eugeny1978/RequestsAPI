import requests                         # библиотека для создания и обработки запросов
from auth import basic_auth             # Аутентификация
from constans import BASE_URL           # Базовый URL
from common_methods import write_data   # запись информации в файлы

def get_trades(order: str, pairId=0, offset=0, limit=10):
    """
    pairId=0 - все пары # 24 - del_usdt
    ccxt/tradesOfUser?limit=10&offset=0&order=<string>&pairId=<integer>
    """

    end_point = f'{BASE_URL}/ccxt/tradesOfUser?limit={limit}&offset={offset}&order={order}&pairId={pairId}'
    responce = requests.post(url=end_point, auth=basic_auth)

    data = responce.json()
    name_file = f'trades_of_user'
    write_data(data, name_file)

    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    data = get_trades('order', pairId=0, offset=0, limit=10)
    if data['ok']:
        print('Получил список Сделок (см. файл json')
    else:
        print('Что-то пошло не так...')

if __name__ == '__main__':
    main()