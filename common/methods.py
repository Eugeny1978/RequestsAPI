import json
from pathlib import Path

# Запись Данных, полученных из запросов
def write_data(data, name_file):
    cwd = Path.cwd() # текущая Папка Исполняемого файла
    relative_path = f'json_responces/{name_file}.json'
    path_to_file = (cwd / relative_path).resolve()
    try:
        with open(path_to_file, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    except Exception as error:
        print(error)