import requests                         # библиотека для создания и обработки запросов
import json                             # библиотека для обработки данных json
from config import BASE_URL, basic_auth # конфигурационные данные
from config import write_json_file      # запись информации в файлы

def get_balance():
    end_point = f'{BASE_URL}/ccxt/balance'
    responce = requests.get(url=end_point, auth=basic_auth)
    data = responce.json()
    name_file = 'get_balance'
    write_json_file(data, name_file)
    return data

def get_types_balance(data: json):
    data = data['result']
    data_free = get_data_format(data, 'free')
    data_used = get_data_format(data, 'used')
    data_total = get_data_format(data, 'total')
    return (data_free, data_used, data_total)

# Получаю Баланс без пустой информации
def get_data_format(data: dict, t): # t in ('free', 'used', 'total')
    data = data[t]
    data_format = {}
    for key in data.keys():
        if data[key] != '0':
            data_format[key] = data[key]
    result = {t:data_format}
    return result


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    data = get_balance()
    print(data)
    my_balance = get_types_balance(data)
    print('Мой Баланс: ..............................')
    for i in my_balance:
        print(i)
    print('..........................................')

if __name__ == '__main__':
    main()