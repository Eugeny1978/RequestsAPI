import api_bitteam.api_keys as keys

PAIR = 'del_usdt' # Торгуемая Пара
RATE_AMOUNT = 1.5 # Коэфициент нарастания Объема
SECTION_DEPO = 50 # Доля Торгуемого Капитала от Общего Депо в %

# api_bitteam.pair # Запрос pair
# date['result']['baseStep'] = 8 # int | Объем q (amount) Знаков после точки
# date['result']['pair']['settings']['lot_size_view_min'] = 6 Знаков после точки
# date['result']['pair']['settings']['price_view_min'] = 6 Знаков после точки
# date['result']['pair']['settings']['limit_usd'] = '0.1' str | Минимальный объем эквивалентен

STEP_AMOUNT = 6 # ШАГ Объемов. Округлять до Знаков после точки
STEP_PRICE = 6  # ШАГ Цен. Округлять до Знаков после точки

def get_api_keys(account):
    if account == 'Account_01':
        API = keys.API
        PRIVATE = keys.PRIVATE
    elif account == 'Account_02':
        API = keys.API_02
        PRIVATE = keys.PRIVATE_02
    elif account == 'Account_03':
        API = keys.API_03
        PRIVATE = keys.PRIVATE_03
    return (API, PRIVATE)


