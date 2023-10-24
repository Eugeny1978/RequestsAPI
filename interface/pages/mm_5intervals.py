import streamlit as st
import sqlite3 as sq                            # Библиотека  Работа с БД
# from data_bases.path_to_base import PATH        # Путь к БД
# from data_bases.path_to_base import PATH

# В терминале набрать:
# streamlit run interface/app.py

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")
st.title('Торговая система: Маркет Мейкинг: 5 Уровней')
st.markdown("---" ) # разделительная линия

PATH = "F:/! PYTON/PyCharm/RequestsAPI/data_bases/base.db"
with sq.connect(PATH) as connect_db:
    cursor_db = connect_db.cursor()
    cursor_db.execute("""SELECT name FROM pairs ORDER BY name""")
    pairs = []
    for pair in cursor_db:
        pairs.append(pair[0])

columnA, columnB = st.columns(2)

pair = columnA.selectbox('Торгумая ПАРА:', options=pairs, index=10)
min_spred = columnA.number_input('Минимальный Спред', min_value=0)
# volume = st.sidebar.number_input('Используемый Объем', min_value=0, max_value=100)
# stop_factor = st.sidebar.number_input('Стоп-фактор', min_value=0, max_value=100)
section_depo = columnB.slider('Тогруемый Объем (% от Средств на депозите):', min_value=0, max_value=100, value=50, step=5)
stop_factor = columnB.slider('Стоп-фактор (% от используемого Объема):', min_value=0, max_value=100, value=20)

result_script = '+2.74%'

run_options = ('Run', 'Pause', 'Stop')
run_script = columnA.radio('Сессия Скрипта:', options=run_options, index=2)
if run_script == 'Run':
    columnA.write('Скрипт Запущен')
elif run_script == 'Pause':
    columnA.write('Скрипт на Паузе (Текущие Ордера не Удалены)')
else:
    result_script = '+0.00%'
    columnA.write('Скрипт Остановлен')

columnB.metric('Текущий Результат:', value=result_script)

st.markdown("---" ) # разделительная линия

st.markdown('<h4>Схема Логики Скрипта</h4>', unsafe_allow_html=True)
st.image('streamlit/media/scheme.png') # caption='Это схема логики'
st.markdown('<h4>Описание Логики Скрипта</h4>', unsafe_allow_html=True)
st.caption('Звуковые комментарии к Торговой Системе')
st.audio('streamlit/media/comment.ogg')
st.text('''Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
Здесь будет текст с описанием.
''')




