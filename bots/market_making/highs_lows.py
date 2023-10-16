import pandas as pd                             # Операции для Таблицы Данных
from api_xt.kline import get_kline              # API Запрос Исторические Свечи
from bots.market_making.config import SYMBOL    # Торгуемая Пара

def get_high_low_interval(interval, dump_json=False):
    data = get_kline(symbol=SYMBOL, limit=2, interval=interval, dump_json=dump_json)
    high = max(float(data['result'][1]['h']), float(data['result'][0]['h']))
    low = min(float(data['result'][1]['l']), float(data['result'][0]['l']))
    return (high, low)

def get_highs_lows(dump_json=False) -> pd.DataFrame:
    intervals = ['4h', '12h', '1d', '3d', '1w']
    df = pd.DataFrame(columns=['high', 'low'])
    for i in intervals:
        high, low = get_high_low_interval(i, dump_json=dump_json)
        df.loc[i] = [high, low]
        # df.loc[intervals.index(i)] = [high, low]

    return df

# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    df = get_highs_lows(dump_json=True)
    print(df)

if __name__ == '__main__':
    main()

