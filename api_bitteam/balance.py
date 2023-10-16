import requests                         # библиотека для создания и обработки запросов
import json                             # библиотека для обработки данных json
from auth import basic_auth             # Аутентификация
from constans import BASE_URL           # Базовый URL
from common.methods import write_data   # запись информации в файлы

def get_balance():
    """
    Баланс по счету
    :return: Данные Запроса в json Словаре
    """
    end_point = f'{BASE_URL}/ccxt/balance'
    responce = requests.get(url=end_point, auth=basic_auth)
    data = responce.json()
    name_file = 'get_balance'
    write_data(data, name_file)
    return data

# Получаю Баланс без пустой информации (Прикладной Метод)
def get_data_format(data: dict, t): # t in ('free', 'used', 'total')
    data = data[t]
    data_format = {}
    for key in data.keys():
        if data[key] != '0':
            data_format[key] = data[key]
    result = {t:data_format}
    return result

def get_types_balance(data: json):
    data = data['result']
    data_free = get_data_format(data, 'free')
    data_used = get_data_format(data, 'used')
    data_total = get_data_format(data, 'total')
    return (data_free, data_used, data_total)


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    data = get_balance()
    # print(data)
    my_balance = get_types_balance(data)
    print('Мой Баланс: ..............................')
    for i in my_balance:
        print(i)
    print('..........................................')

if __name__ == '__main__':
    main()