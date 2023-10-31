import os
import signal
import subprocess                               # Запуск внешних скриптов
import sqlite3 as sq                            # Библиотека  Работа с БД
from time import sleep
from data_bases.path_to_base import PATH

my_env = os.environ.copy()
env_path = my_env['PATH']
env_pyton = my_env['PYTHONPATH']
# PYTHONPATH : "F:\! PYTON\PyCharm\RequestsAPI"
# print(my_env)
# my_env["PATH"] = f"/usr/sbin:/sbin:{my_env['PATH']}"
# subprocess.Popen(my_command, env=my_env)


# def run_bot():
#     cmd = "python ../bots/mm_5intervals/test_bot.py"
#     bot = subprocess.Popen(cmd)
#     set_bot_pid(bot.pid)

def run_bot():
    cmd = "python ../bots/mm_5intervals/test_bot.py"
    bot = subprocess.Popen(cmd, env=my_env) # , stdout=subprocess.PIPE, shell=True, env=env_pyton, env=my_env,
    # stdout=subprocess.PIPE, stderr=subprocess.PIPE
    set_bot_pid(bot.pid)

def kill_bot(pid): #
    os.kill(pid, signal.SIGTERM) #  SIGSTOP SIGKILL SIG_BLOCK SIGCHLD SIGCLD SIGPIPE CTRL_C_EVENT CTRL_BREAK_EVENT
    # Отрабатывают: SIGABRT SIGTERM SIGBREAK SIGINT
    # os.kill(pid, 0)

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
sleep(5)
print(get_bot_pid())
kill_bot(get_bot_pid())
print('Процесс Прерван!')

run_bot()
sleep(5)
kill_bot(get_bot_pid())
print('Процесс Прерван!')



# НЕПРАВИЛЬНО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

# # ---- # Конструкция для выполнения кода ТОЛЬКО из этого файла -----------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()



