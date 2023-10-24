import requests                             # Библиотека для создания и обработки запросов
from api.request import Request             # Базовый Класс


BASE_URL = 'https://sapi.xt.com'

class RequestXT(Request):

    def get_depth(self, symbol='del_usdt', limit=500, dump_json=False):
        """
        Стакан Цен по выбранной Паре (Символ)
        """
        limit_url = '' if limit == 50 else f'&limit={limit}'
        point = '/v4/public/depth'
        end_point = f'{BASE_URL}{point}?symbol={symbol}{limit_url}'

        dt_now = self.get_moment_date()
        responce = requests.get(url=end_point)

        self.status = responce.status_code
        self.date = responce.json()
        self.file_name = f'XT_depth_{symbol}_{dt_now}'

    def get_kline(self, symbol='del_usdt', interval='1d', limit=100, startTime=0, endTime=0):
        """
        Получение Свечей. 0-ая Свеча - текущая (незакрытая)
        symbol - обязательный
        interval - обязательный - [1m;3m;5m;15m;30m;1h;2h;4h;6h;8h;12h;1d;3d;1w;1M]
        limit - Необязательный
        startTime, endTime - Необязательный timestamp number
        """
        # Необязательные Параметры
        url_limit = '' if limit == 100 else f'&limit={limit}'
        url_startTime = '' if not startTime else f'&startTime={startTime}'
        url_endTime = '' if not endTime else f'&endTime={endTime}'

        point = '/v4/public/kline'
        end_point = f'{BASE_URL}{point}?symbol={symbol}&interval={interval}' + url_limit + url_startTime + url_endTime
        dt_now = self.get_moment_date()
        responce = requests.get(url=end_point)

        self.status = responce.status_code
        self.data = responce.json()
        self.file_name = f'XT_kline_{symbol}_{interval}_{limit}_{dt_now}'





# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():
    req = RequestXT()

    # req.get_depth() # Получение Стакана Цен
    req.get_kline(limit=2) # Получение Свечек

    print(req.__dict__) # Вывод на экран Атрибутов Экземляра Класса
    req.write_data() # Запись Данных в файл

if __name__ == '__main__':
    main()