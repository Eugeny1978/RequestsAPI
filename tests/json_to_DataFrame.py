import requests                         # библиотека для создания и обработки запросов
import json                             # библиотека для обработки данных json
from config import BASE_URL, basic_auth # конфигурационные данные
from config import write_json_file      # запись информации в файлы
from time import sleep                  # пауза

import pandas as pd
from balance import get_balance, get_types_balance


# # Creating dataframe from dictionary object.
# import pandas as pd
# data = [{'name': 'vikash', 'age': 27}, {'name': 'Satyam', 'age': 14}]
# df = pd.DataFrame.from_dict(data, orient='columns')
# df
#
# Out[4]:
#    age  name
# 0   27  vikash
# 1   14  Satyam
#
# # If you have nested columns then you first need to normalize the data:
# data = [
#   {
#     'name': {
#       'first': 'vikash',
#       'last': 'singh'
#     },
#     'age': 27
#   },
#   {
#     'name': {
#       'first': 'satyam',
#       'last': 'singh'
#     },
#     'age': 14
#   }
# ]
# df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
# df
# Out[8]:
# age name.first  name.last
# 0   27  vikash  singh
# 1   14  satyam  singh


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    data = get_balance()
    df = pd.DataFrame.from_dict(data, orient='columns')
    print(df)

    # РАзворачивает вложенные словари (столбцы)
    df_normalize = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
    print(df_normalize)

    # my_balance = get_types_balance(data)
    # df_my_balance = pd.DataFrame.from_dict(my_balance, orient='columns')
    # print(df_my_balance)

    json_normalize = pd.json_normalize(data)
    print('\n Normalize')
    print(json_normalize)


if __name__ == '__main__':
    main()