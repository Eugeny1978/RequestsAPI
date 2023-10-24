import api_bitteam.api_keys as keys

PAIR = 'del_usdt' # Торгуемая Пара
INTERVALS = ['4h', '12h', '1d', '3d', '1w']
SECTION_DEPO = 20 # Доля Торгуемого Капитала от Общего Депо в %
ACCOUNT = {'name': 'Luchnik78', 'exchange': 'Bitteam'}
RATE_AMOUNT = 1.5 # Коэфициент нарастания Объема
STEP_PRICE = 6  # ШАГ Цен. Округлять до Знаков после точки
STEP_AMOUNT = 6 # ШАГ Объемов. Округлять до Знаков после точки
STATUS_RUN = True # Статус Запущен или остановлен Скрипт

# api_bitteam.pair # Запрос pair
# date['result']['baseStep'] = 8 # int | Объем q (amount) Знаков после точки
# date['result']['pair']['settings']['lot_size_view_min'] = 6 Знаков после точки
# date['result']['pair']['settings']['price_view_min'] = 6 Знаков после точки
# date['result']['pair']['settings']['limit_usd'] = '0.1' str | Минимальный объем эквивалентен

# STEP_AMOUNT = 6 # ШАГ Объемов. Округлять до Знаков после точки
# STEP_PRICE = 6  # ШАГ Цен. Округлять до Знаков после точки
