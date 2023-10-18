import json                                 # Библиотека Обработки json Объектов
import jsonpickle                           # Библиотека Обработки json Объектов
from pathlib import Path                    # Библиотека Определения Пути к файлу
from datetime import datetime               # Для момента в который снимаем информацию по Запросу



class Request:
    def __init__(self):
        self.status = 0
        self.data = {}
        self.file_name = ''
        self.auth = ''

    # Момент времени Получения данных из Запроса
    def get_moment_date(self):
        dt_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return dt_now

    # Запись Данных, полученных из запросов
    def write_data(self):

        if self.status != 200:
            print('Что-то пошло не так. Запрос не имеет статус "200"')
            pass

        file_name = self.file_name.split('/')[-1]
        print(f'Данные Запроса записаны в файл: {file_name}')
        cwd = Path.cwd()  # текущая Папка Исполняемого файла
        relative_path = f'json_responces/{self.file_name}.json'
        path_to_file = (cwd / relative_path).resolve()

        # Преобразую Словарь dict() в Объект формата JSON
        data_json = jsonpickle.encode(self.data, indent=4,make_refs=False)

        try:
            with open(path_to_file, 'w') as file:
                # json.dump(data_json, self.file_name, indent=4, sort_keys=True)
                file.write(data_json)
        except Exception as error:
            print(error.__class__, error)