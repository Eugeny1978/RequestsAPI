import json

# Запись Данных, полученных из запросов
def write_data(data, name_file):
    path_to_file = f'json_responces/{name_file}.json'
    try:
        with open(path_to_file, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)
    except Exception as error:
        print(error)