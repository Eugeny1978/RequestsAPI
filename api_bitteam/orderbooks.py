import requests                         # библиотека для создания и обработки запросов
from constans import BASE_URL           # Базовый URL
from common_methods import write_data   # запись информации в файлы
from datetime import datetime           # для момента в который снимаем слепок стакана


def get_orderbooks(pair='del_usdt'):
    """
    Стакан Цен по выбранной Паре
    Также Стакан есть и в запросе "pair". Но там он обрезан лимитом в 50 слотов
    """
    end_point = f'{BASE_URL}/orderbooks/{pair}'
    dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    responce = requests.get(url=end_point)
    data = responce.json()
    name_file = f'orderbooks_{pair}_{dt_now}'
    write_data(data, name_file)
    return data

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    get_orderbooks()
    get_orderbooks('del_usdt')


if __name__ == '__main__':
    main()