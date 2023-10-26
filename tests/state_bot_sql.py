import sqlite3 as sq                        # Библиотека для работы с БД
from data_bases.path_to_base import PATH

def get_state_bot():
    """
    :return: bool
    """
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("SELECT state FROM bot_mm5_levels ORDER BY rowid DESC")
        return bool(curs.fetchone()[0])

def set_state_bot(state):
    """
    state - любое значение. Если Истина присвоит 1, если Ложь присвоит 0
    state_int in (1, 0)
    """
    state_int = 1 if state else 0
    with sq.connect(PATH) as connect:
        curs = connect.cursor()
        curs.execute("UPDATE bot_mm5_levels SET state = :State", {'State': state_int})



set_state_bot(1)
print(get_state_bot())

set_state_bot(True)
print(get_state_bot())

set_state_bot(5)
print(get_state_bot())

set_state_bot(0)
print(get_state_bot())

set_state_bot(False)
print(get_state_bot())

set_state_bot(55+55)
print(get_state_bot())