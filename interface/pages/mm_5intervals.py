import streamlit as st                          # Библиотека Компоновщик Страниц Интерфейся
import sqlite3 as sq                            # Библиотека  Работа с БД
import pandas as pd                             # Преобразовать Словари в Таблицы
import subprocess, os, signal                   # Запуск внешних скриптов

import sys
sys.path.append('.')
from data_bases.path_to_base import PATH        # Путь к БД


# В терминале набрать:
# streamlit run interface/app.py

# --- СЕРВИСНЫЕ ФУНКЦИИ -------------------------------------------------------

def get_state_bot():
    """
    :return: bool
    """
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("SELECT state FROM bot_mm_5_intervals ORDER BY rowid DESC")
        return bool(curs.fetchone()[0])

def set_state_bot(state):
    """
    state - любое значение. Если Истина присвоит 1, если Ложь присвоит 0
    state_int in (1, 0)
    """
    state_int = 1 if state else 0
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("UPDATE bot_mm_5_intervals SET state = :State", {'State': state_int})

def run_bot():
    # cmd = "python bots/mm_5intervals/test_bot.py"
    cmd = "python bots/mm_5intervals/ts.py"
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
    # cmd = "python bots/mm_5intervals/test_cancel_orders.py"
    cmd = "python bots/mm_5intervals/cancel_orders.py"
    subprocess.Popen(cmd)



# --- КОНЕЦ СЕРВИСНЫХ ФУНКЦИЙ -------------------------------------------------------

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")
# st.title('Торговая система: Маркет Мейкинг: 5 Уровней')
st.subheader('Торговая система: Маркет Мейкинг: 5 Уровней')
st.markdown("---" ) # разделительная линия

# PATH = "F:/! PYTON/PyCharm/RequestsAPI/data_bases/base.db"
with sq.connect(PATH) as connect:
    # connect.row_factory = sq.Row  # Если хотим строки записей в виде dict {}. По умолчанию - кортежи turple ()
    curs = connect.cursor()

    curs.execute("""SELECT name FROM pairs ORDER BY name""")
    pairs = []
    for pair in curs:
        pairs.append(pair[0]) # 'name'

    curs.execute("""SELECT * FROM trade_api ORDER BY name""")
    # accounts = pd.DataFrame(columns=['name', 'exchange', 'public_key', 'secret_key'])
    accounts = []
    for account in curs:
        # accounts.loc[len(accounts.index)] = [account['name'], account['exchange'], account['public_key'], account['secret_key']]
        accounts.append((account[0], account[1]))

columnA, columnB, columnC = st.columns(3)

trade_account = columnA.selectbox('Торговый Аккаунт:', options=accounts) # index=0
dict_account = {'name': trade_account[0], 'exchange': trade_account[1]}
pair = columnA.selectbox('Торгумая ПАРА:', options=pairs, index=10)
rate_amount = columnA.number_input('Коэфициент нарастания Объема', min_value=0.0,value=1.5, step=0.1, format='%f')
section_depo = columnA.slider('Торгуемый Объем (% от Средств на депозите):', min_value=0, max_value=100, value=50, step=5)

def dump_parameters():
    try:
        with open('bots/mm_5intervals/config.py', "w+", encoding='utf-8') as file:
            constant_text = f"""# Настраиваемые Параметры -----------------------------
ACCOUNT = {dict_account}      # Торговый Акканут
PAIR = '{pair}'               # Торгуемая Пара
RATE_AMOUNT = {rate_amount}   # Коэфициент нарастания Объема
SECTION_DEPO = {section_depo} # Доля Торгуемого Капитала от Общего Депо в %
# НЕ Настраиваемые Параметры ---------------------------
INTERVALS = ['4h', '12h', '1d', '3d', '1w']
STEP_PRICE = 6    # ШАГ Цен. Округлять до Знаков после точки
STEP_AMOUNT = 6   # ШАГ Объемов. Округлять до Знаков после точки
STATUS_RUN = True # Статус Запущен или остановлен Скрипт
"""
            file.write(constant_text)
    except Exception as error:
        print(error.__class__, error)
    # Дублирование инфы в csv файл для актуального отображения сохраненных параметров
    df_dict = {'ACCOUNT': dict_account['name'],
                'PAIR': pair,
                'RATE_AMOUNT': rate_amount,
               'SECTION_DEPO': section_depo}
    df = pd.DataFrame(df_dict, index=['value'])
    try:
        df.to_csv('df.csv', index=False)
    except Exception as error:
        print(error.__class__, error)

dump_config = columnB.button('Записать Выбранные Параметры в Конфигурационный Файл', on_click=dump_parameters)
try:
    df = pd.read_csv('df.csv')
    columnB.dataframe(df, hide_index=True)
except Exception as error:
    print(error.__class__, error)

run_options = ('Run', 'Pause', 'Stop')
run_script = columnB.radio('Сессия Скрипта:', options=run_options, index=2) # on_change=radio_change

if run_script == 'Run':
    if not get_state_bot():
        run_bot() # Запускаю БОТ
        set_state_bot(True)
    columnB.write('Скрипт Запущен')
elif run_script == 'Pause':
    if get_state_bot():
        kill_bot(get_bot_pid()) # Останавливаю БОТ
        set_state_bot(False)
    columnB.write('Скрипт на Паузе (Выставленные Ордера Активны (не удалены)')
else:
    if get_state_bot():
        kill_bot(get_bot_pid()) # Останавливаю БОТ
        set_state_bot(False)
    cancel_orders_bot()  # Запускаю БОТ, удаляющий Ордера
    columnB.write('Скрипт Остановлен. (Выставленные Ордера Удалены)')


columnC.markdown('<h4>Схема Логики Скрипта</h4>', unsafe_allow_html=True)
columnC.image('interface/media/scheme.png') # caption='Это схема логики'
st.markdown("---" ) # разделительная линия

st.text('''
1. Определяются 5 уровней, на которых будут установлены Ордера.
Используются Временные Интервалы: ['4h', '12h', '1d', '3d', '1w']
Уровни на Покупку (BUY)   - от максимумов
Уровни на Продажу (SELL)  - от минимумов

2. Определяется Объемы Ордеров, исходя из заданного % Используемого капитала
и наличия Свободных Крипто-Монет для Указанного Счета и Торгуемой Паре(монет).
При распределении Средства по ордерам Используется Коэфициент Нарастания Объема: RATE_AMOUNT
level_0 = X
level_1 = RATE_AMOUNT * X
level_2 = RATE_AMOUNT**2 * X
level_3 = RATE_AMOUNT**3 * X
level_4 = RATE_AMOUNT**4 * X
Если задать RATE_AMOUNT > 1 - то каждый следующий уровень будет иметь более массивный объем (нарастание объема)
Если задать RATE_AMOUNT < 1 - то каждый следующий уровень будет иметь менее массивный объем (снижение объема)
Если задать RATE_AMOUNT = 1 - объем распределится равномерно по уровням

3. Выставляются ордера. С корректировкой (сдвигом) Уровней на Указаннный в конфигурационном файле Шаг для 
BUY  - цены НИЖЕ на Шаг от уровней.
SELL - цены ВЫШЕ на Шаг от уровней.
''')


