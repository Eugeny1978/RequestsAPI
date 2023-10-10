import requests
import json

base_url = 'https://yobit.net'
ignore = '?ignore_invalid=1'  # на случай если перечисленные пары не торгуются

def write_json_file(data, name_file):
    path_to_file = f'json_youtube/{name_file}.json'
    try:
        with open(path_to_file, 'w') as file:
            json.dump(data, file, sort_keys=True)
    except Exception as error:
        print(error)

def get_info():
    end_point = base_url + '/api/3/info'
    responce = requests.get(url=end_point)
    data_json = responce.json()
    write_json_file(data_json, 'get_info')
    return data_json

def get_ticker(pairs):
    end_point = base_url + '/api/3/ticker/' + pairs + ignore
    responce = requests.get(url=end_point)
    data_json = responce.json()
    name_file = f'get_ticker_{pairs}'
    write_json_file(data_json, name_file)
    return data_json

def get_ticker_coin(coin1='btc', coin2='usd'):
    end_point = base_url + '/api/3/ticker/' + coin1 + '_' + coin2 + ignore
    responce = requests.get(url=end_point)
    data_json = responce.json()
    name_file = f'get_ticker_coin_{coin1}_{coin2}'
    write_json_file(data_json, name_file)
    return data_json

def get_depth(coin1='eth', coin2='usdt', limit=100): # limit - количество интекрвалов
    end_point = f'{base_url}/api/3/depth/{coin1}_{coin2}?limit={limit}&{ignore}'
    responce = requests.get(url=end_point)
    data_json = responce.json()
    name_file = f'get_depth_{coin1}_{coin2}_limit_{limit}'
    write_json_file(data_json, name_file)
    return data_json

def get_total_bids(coin1='btc', coin2='usdt'):
    bids = get_depth(coin1, coin2, limit=2500)[f'{coin1}_{coin2}']['bids']
    total_bids_amount = 0
    for i in bids:
        price = i[0]
        coin_amount = i[1]
        total_bids_amount += price*coin_amount
    return total_bids_amount

def get_average_price(coin1='btc', coin2='usdt', side='bids', limit=100): # side='asks'

    slots = get_depth(coin1, coin2, limit)[f'{coin1}_{coin2}'][side]

    total_amount = 0
    for i in slots:
        total_amount += i[1]

    total_slots = 0
    for j in slots:
        price = j[0]
        coin_amount = j[1]
        total_slots += price * coin_amount
    average_price = total_slots / total_amount

    return average_price







#--- RUN2 -----------------------------------------------

def main():
    print(get_info())
    # pairs = 'eth_usdt-btc_usdt'  # если одна то '/eth_usdt'
    # print(get_ticker(pairs))
    # print(get_ticker_coin('dash', 'usd'))
    # print(get_depth('xrp', 'usdt', 2500))
    # print(get_total_bids(coin1='btc', coin2='usdt'))

    # av_bid_100 = get_average_price(coin1='btc', coin2='usdt', side='bids', limit=100)
    # av_bid_max = get_average_price(coin1='btc', coin2='usdt', side='bids', limit=2500)
    # av_ask_100 = get_average_price(coin1='btc', coin2='usdt', side='asks', limit=100)
    # av_ask_max = get_average_price(coin1='btc', coin2='usdt', side='asks', limit=2500)
    # print(f'Aver BTC-USDT (100 slot) || Bid: {av_bid_100: .4f} | Ask: {av_ask_100: .4f}')
    # print(f'Aver BTC-USDT (max slot) || Bid: {av_bid_max: .4f} | Ask: {av_ask_max: .4f}')



if __name__ == '__main__':
    main()

# --- RUN1 ----------------------------------------------

