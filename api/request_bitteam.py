import requests                             # Библиотека для создания и обработки запросов
from api.request import Request             # Базовый Класс


BASE_URL = 'https://bit.team/trade/api'

class RequestBitTeam(Request):

    def get_orderbooks(self, pair='del_usdt'):
        """
        Стакан Цен по выбранной Паре
        Также Стакан есть и в запросе "pair". Но там он обрезан лимитом в 50 слотов
        """
        end_point = f'{BASE_URL}/orderbooks/{pair}'

        dt_now = self.get_moment_date()
        responce = requests.get(url=end_point)

        self.status = responce.status_code
        self.date = responce.json()
        self.file_name = f'BitTeam_orderbooks_{pair}_{dt_now}'


    def get_pair(self, pair='del_usdt'):
        """
        Весь Стакан есть и в запросе "orderbooks". Здесь он обрезан лимитом в 50 слотов

        """
        end_point = f'{BASE_URL}/pair/{pair}'

        dt_now = self.get_moment_date()
        responce = requests.get(url=end_point)

        self.status = responce.status_code
        self.date = responce.json()
        self.file_name = f'BitTeam_pair_{pair}_{dt_now}'


# ---- # Конструкция для выполнения кода из этого файла -----------------------------------------
def main():

    req = RequestBitTeam()

    # req.get_orderbooks()   # Получение Стакана Цен
    req.get_pair()         # Информация по Торгуемой Паре
    print(f"Шаг Размера Лота: {req.date['result']['pair']['baseStep']}")  # Мин. шаг размера Лота. Кол-во знаков в Дроби после целой части. int()
    print(f"ЦЕНА. Кол-во Знаков после целой части: {req.date['result']['pair']['settings']['price_view_min']}") # Кол-во знаков в Дроби после целой части. str()
    print(f"Размер Позы. Кол-во Знаков после целой части: {req.date['result']['pair']['settings']['lot_size_view_min']}") # Кол-во знаков в Дроби после целой части. str()
    print(f"Мин. Размер Позы в USD: {req.date['result']['pair']['settings']['limit_usd']}") # Мин. размер Лота относительно Доллара US. str()


    # print(req.__dict__)  # Вывод на экран Атрибутов Экземляра Класса
    # req.write_data()  # Запись Данных в файл


if __name__ == '__main__':
    main()