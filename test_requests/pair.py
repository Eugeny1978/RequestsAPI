import requests                         # библиотека для создания и обработки запросов
import json                             # библиотека для обработки данных json
from config import BASE_URL             # конфигурационные данные
from config import write_json_file      # запись информации в файлы


def get_pair_info(pair): # eth_usdt
    end_point = f'{BASE_URL}/pair/{pair}'
    responce = requests.get(url=end_point) # query=dict
    data = responce.json() # responce.text
    write_json_file(data, f'pair_info_{pair}')
    return data


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    pair = 'eth_usdt'
    print(get_pair_info(pair))

if __name__ == '__main__':
    main()