import os

# Добиться результата:
# F:\! PYTON\PyCharm\RequestsAPI\data_bases\base.db

# Имя Файла Базы Данных (БД)
base_name = 'base.db'
# Папка данного файла. В этой же папке находится и файл БД
folder = os.path.dirname(repr(__file__)).replace("'", '')

# PATH = folder + '\\\\' + base_name # тоже работает, но предпочел чтобы с одной чертой
path_to_file = (folder + '\\\\' + base_name)
PATH = rf'{path_to_file}'.replace('\\\\', '/')

# print(PATH)




