import os
import signal
import subprocess                               # Запуск внешних скриптов
import psutil                                   # Инфо и Управление запущенными процессами
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
    # cmd = "python ../bots/mm_5intervals/test_bot.py"
    # bot = subprocess.Popen(cmd, shell=True, close_fds=True) # , stdout=subprocess.PIPE, shell=True, env=env_pyton, env=my_env start_new_session=True cwd: # stdout=subprocess.PIPE, stderr=subprocess.PIPE
    cmd = "python test_bot.py"
    temp_cwd = '../bots/mm_5intervals/'
    bot = subprocess.Popen(cmd, cwd=temp_cwd, shell=True)  # , start_new_session=True
    set_bot_pid(bot.pid)
    # aaa = os.getpgid(bot.pid)
    # print(aaa)


# def kill_bot(pid): #
#     os.kill(pid, signal.SIGINT)
#     # Отрабатывают: SIGABRT SIGTERM SIGBREAK SIGINT
#     # НЕ отрабатывают: SIGSTOP SIGKILL SIG_BLOCK SIGCHLD SIGCLD SIGPIPE CTRL_C_EVENT CTRL_BREAK_EVENT
#     print('Процесс Прерван!')


def kill_bot(pid):
    '''Kills parent and children processes'''
    parent = psutil.Process(pid)
    # --- kill all the child processes
    for child in parent.children(recursive=True):
        # print(f'child: {child}')
        child.kill()
        # --- kill the parent process
        # print(f'parent: {parent}')
        # parent.kill()
    # В моем случае Не нужно Автоматически уничтожается при удалении Дочерних Процессов.
    # Соответственно вызовет Ошибку прр попытке
    # os.kill(pid, signal.SIGTERM)
    # # Отрабатывают: SIGABRT SIGTERM SIGBREAK SIGINT
    # # НЕ отрабатывают: SIGSTOP SIGKILL SIG_BLOCK SIGCHLD SIGCLD SIGPIPE CTRL_C_EVENT CTRL_BREAK_EVENT
    print('Процесс Прерван!')

# def kill_processes(pid):
#     '''Kills parent and children processess'''
#     parent = psutil.Process(pid)
#     # kill all the child processes
#     for child in parent.children(recursive=True):
#         print(child)
#         child.kill()
#         # kill the parent process
#         print(parent)
#         parent.kill()
#
# # remember to assign subprocess to a variable
# pro = subprocess.Popen("python3 write_to_file.py", stdout=subprocess.PIPE,
#                        shell=True, start_new_session=True)
#
# # get the process id
# print("Process ID:", pro.pid)
#
# # call function to kill all processes in a group
# kill_processes(pro.pid)



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
    subprocess.Popen(cmd, shell=True)




# # ---- # Конструкция для выполнения кода ТОЛЬКО из этого файла -----------------------------------------
def main():
    run_bot()
    sleep(5)
    # kill_bot(get_bot_pid())
    kill_bot(get_bot_pid())


    run_bot()
    sleep(5)
    # kill_bot(get_bot_pid())
    kill_bot(get_bot_pid())

# -----------------------------------


if __name__ == '__main__':
    main()



