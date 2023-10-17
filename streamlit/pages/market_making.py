import streamlit as st

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")
st.title('Торговая система: Market-Making')
st.markdown("---" ) # разделительная линия

# m = st.markdown("""<style>div.stButton > button:first-child {background-color: rgb(188, 245, 188);}</style>""", unsafe_allow_html=True)
# m = st.markdown("""<style>div.stButton > button:first-child {background-color: rgb(255, 232, 219);}</style>""", unsafe_allow_html=True)

columnA, columnB = st.columns(2)

pairs = ('del_usdt', 'farms_usdt', 'eth_usdt')
pair = columnA.selectbox('Торгумая ПАРА:', options=pairs)
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




