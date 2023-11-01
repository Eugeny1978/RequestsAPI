import sys
sys.path.append('.')

from api.request_bitteam import RequestBitTeam  # Класс запросы (BitTeam)
from bots.mm_5intervals.config_old import PAIR, ACCOUNT # Конфигурационные Параметры
aaa = PAIR
bbb = ACCOUNT
ccc = RequestBitTeam()

from time import sleep

i = 1
while True:
    print(f'Выполняется Файл Скрипта | {i}-цикл')
    sleep(2)
    i += 1
