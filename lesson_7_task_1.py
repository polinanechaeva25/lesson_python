import os
from sys import argv

# Для создания нужного количества вложенных папок через терминал
# Название внешней директории - argv[1] = my_project
# Первая внутренняя директоия - argv[2] = settings
# argv[3] - количество дополнительных новых директоий = 3
# argv[i] - названия следующих вложенных директории = mainapp adminapp authapp
dir_path = os.path.join(argv[1], argv[2])
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
if len(argv) > 3:
    os.chdir(argv[1])
    for i in range(int(argv[3])):
        if not os.path.exists(argv[i+4]):
            os.mkdir(argv[i+4])
