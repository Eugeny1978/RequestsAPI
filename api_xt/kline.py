import requests                         # библиотека для создания и обработки запросов
from common.methods import write_data   # запись информации в файлы
from datetime import datetime           # для момента в который снимаем информацию
from constants import BASE_URL          # Базовый URL

def get_kline(symbol='del_usdt', interval='1d', limit=100, startTime=0, endTime=0):
    """
    symbol - обязательный
    interval - обязательный - [1m;3m;5m;15m;30m;1h;2h;4h;6h;8h;12h;1d;3d;1w;1M]
    limit - Необязательный
    startTime, endTime - Необязательный timestamp number

    """
    # Необязательные Параметры
    url_limit = '' if limit == 100 else f'&limit={limit}'
    url_startTime = '' if not startTime else f'&startTime={startTime}'
    url_endTime = '' if not endTime else f'&endTime={endTime}'

    point = '/v4/public/kline'
    end_point = f'{BASE_URL}{point}?symbol={symbol}&interval={interval}' + url_limit + url_startTime + url_endTime
    dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    responce = requests.get(url=end_point)
    data = responce.json()
    name_file = f'XT_kline_{symbol}_{interval}_{limit}_{dt_now}'
    write_data(data, name_file)
    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    # data = get_kline(symbol='del_usdt', interval='1d', limit=5)
    data = get_kline(limit=5)

if __name__ == '__main__':
    main()