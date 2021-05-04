import os

path = os.path.abspath('./')
folder_1 = os.path.join(path, 'my_project')
new_folder = os.path.join(folder_1, 'templates')
for obj in os.scandir('my_project'):
    for el in os.scandir(obj):
        if el.name == 'templates':
            folder = os.path.join(path, el)
            for root, dirs, files in os.walk(folder):
                if not os.path.exists(new_folder):
                    path_1 = os.path.join(new_folder, *dirs)
                    os.makedirs(path_1)
                else:
                    path_1 = os.path.join(new_folder, *dirs)
                    if not os.path.exists(path_1):
                        os.mkdir(path_1)
for root, dirs, files in os.walk(folder_1):
    if root.count('templates'):
        for file in files:
            for root_1, dirs_1, files_1 in os.walk(new_folder):
                if not root_1.endswith('templates'):
                    os.chdir(root_1)
                    with open(file, 'w', encoding='utf-8') as f:
                        pass