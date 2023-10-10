import requests                         # библиотека для создания и обработки запросов
import json                             # библиотека для обработки данных json
from time import sleep                  # библиотека для паузы
from config import BASE_URL, basic_auth # конфигурационные данные
from config import write_json_file      # запись информации в файлы
from orders import create_order         # создать ордер

def cancel_all_orders():
    end_point = f'{BASE_URL}/ccxt/cancel-all-order'
    body = {"pairId": 0 } # 1-100 - по конкретной паре || 0 - all pairs
    responce = requests.post(url=end_point, auth=basic_auth, data=body)
    data = responce.json()
    name_file = f'cancel_all_orders'
    write_json_file(data, name_file)






# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    body_order1 = ['44', 'buy', 'limit', '240', '0.030'] # 44 -> farms_usdt
    body_order2 = ['2', 'buy', 'limit', '0.008', '1200'] # 2 -> eth_usdt
    body_order3 = ['24', 'buy', 'limit', '480', '0.015'] # -> del_usdt

    create_order(body_order1[0], body_order1[1], body_order1[2], body_order1[3], body_order1[4])
    create_order(body_order2[0], body_order2[1], body_order2[2], body_order2[3], body_order2[4])
    create_order(body_order3[0], body_order3[1], body_order3[2], body_order3[3], body_order3[4])
    sleep(20)

    cancel_all_orders()

if __name__ == '__main__':
    main()