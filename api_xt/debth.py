import requests                             # библиотека для создания и обработки запросов
from common.methods import write_data       # запись информации в файлы
from datetime import datetime               # для момента в который снимаем информацию
from api_xt.constants import BASE_URL       # Базовый URL, Папка логов

def get_depth(symbol='del_usdt', dump_json=False):
    """
    """
    point = '/v4/public/depth'
    end_point = f'{BASE_URL}{point}?symbol={symbol}&limit=500'
    dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    responce = requests.get(url=end_point)
    data = responce.json()
    name_file = f'XT_depth_{symbol}_{dt_now}'
    write_data(data, name_file, dump_json)
    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    # data = get_depth()
    get_depth('del_usdt', dump_json=True)

if __name__ == '__main__':
    main()