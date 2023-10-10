import requests                         # библиотека для создания и обработки запросов
from config import BASE_URL, basic_auth # конфигурационные данные
from config import write_json_file      # запись информации в файлы
from time import sleep                  # пауза
from datetime import datetime           # для момента в который снимаем слепок стакана


# Также Стакан есть и в запросе pair. Но там он обрезан лимитом в 50 слотов

def get_orderbooks(pair='btc_usdt'):
    """
    """
    end_point = f'{BASE_URL}/orderbooks/{pair}'
    dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    responce = requests.get(url=end_point)
    data = responce.json()
    name_file = f'orderbooks_{pair}_{dt_now}'
    write_json_file(data, name_file)
    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    data = get_orderbooks('eth_usdt')

if __name__ == '__main__':
    main()