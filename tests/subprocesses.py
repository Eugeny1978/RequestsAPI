import os
import signal
import subprocess                               # Запуск внешних скриптов
import sqlite3 as sq                            # Библиотека  Работа с БД
from time import sleep
from data_bases.path_to_base import PATH

def run_bot():
    cmd = "python ../bots/mm_5intervals/test_bot.py"
    bot = subprocess.Popen(cmd)
    set_bot_pid(bot.pid)

def kill_bot(pid):
    os.kill(pid, signal.SIGTERM)

def set_bot_pid(pid):
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("UPDATE bot_mm_5_intervals SET pid = :Pid", {'Pid': pid})
        print(pid)

def get_bot_pid():
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("SELECT pid FROM bot_mm_5_intervals ORDER BY rowid DESC")
        return curs.fetchone()[0]
def cancel_orders_bot():
    cmd = "python ../bots/mm_5intervals/test_cancel_orders.py"
    subprocess.Popen(cmd)

print('ПРАВИЛЬНО! ----------------')
run_bot()
sleep(7)
kill_bot(get_bot_pid())
print('Процесс Прерван!')

run_bot()
sleep(7)
kill_bot(get_bot_pid())
print('Процесс Прерван!')




# print('НЕПРАВИЛЬНО! ----------------')
# bot1 = get_bot()
# pid_1 = bot1.pid
# sleep(7)
# bot1.kill()
# print('Процесс Прерван!')
#
# bot2 = get_bot()
# pid_2 = bot2.pid
# sleep(7)
# bot1.kill()
# print('Процесс Прерван!')
# # os.kill(pid_1, signal.SIGTERM)
# # os.kill(pid_2, signal.SIGTERM)

# print('ПРАВИЛЬНО! ----------------')
# cmd = "python ../bots/mm_5intervals/test_bot.py"
# bot3 = subprocess.Popen(cmd)
# pid_3 = bot3.pid
# print(type(pid_3))
# sleep(7)
# os.kill(pid_3, signal.SIGTERM)
# print('Процесс Прерван!')
#
# bot4 = subprocess.Popen(cmd)
# pid_4 = bot4.pid
# sleep(7)
# os.kill(pid_4, signal.SIGTERM)
# print('Процесс Прерван!')
#
# bot5 = subprocess.Popen(cmd)
# pid_5 = bot5.pid
# sleep(7)
# os.kill(pid_5, signal.SIGTERM)
# print('Процесс Прерван!')

# print('ПРАВИЛЬНО! ----------------')
# cmd = "python ../bots/mm_5intervals/test_bot.py"
# bot = subprocess.Popen(cmd)
# sleep(7)
# bot.terminate()
# print('Процесс Прерван!')
#
# bot = subprocess.Popen(cmd)
# sleep(7)
# bot.terminate()
# print('Процесс Прерван!')


# print('ПРАВИЛЬНО! ----------------')
# bot = run_bot()
# sleep(7)
# os.kill(get_bot_pid(), signal.SIGTERM)
# print('Процесс Прерван!')
#
# bot = run_bot()
# sleep(7)
# os.kill(get_bot_pid(), signal.SIGTERM)
# print('Процесс Прерван!')

# print('ПРАВИЛЬНО! ----------------')
# bot = run_bot()
# sleep(7)
# bot.terminate()
# print('Процесс Прерван!')
#
# bot = run_bot()
# sleep(7)
# bot.terminate()
# print('Процесс Прерван!')



