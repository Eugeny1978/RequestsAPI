import requests                         # библиотека для создания и обработки запросов
from config import write_json_file      # запись информации в файлы
from datetime import datetime           # для момента в который снимаем слепок стакана


BASE_URL =  'https://sapi.xt.com'
point = '/v4/public/depth'

def get_orderbooks(pair='btc_usdt'):
    """
    """
    end_point = f'{BASE_URL}{point}?symbol={pair}&limit=500'
    dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    responce = requests.get(url=end_point)
    data = responce.json()
    name_file = f'orderbooks_XT_{pair}_{dt_now}'
    write_json_file(data, name_file)
    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    data = get_orderbooks('del_usdt')

if __name__ == '__main__':
    main()