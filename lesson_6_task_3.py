import json
import sys

NAMES = ['Иванов,Иван,Иванович\n']
HOBBYS = ['скалолазание,охота\n', 'горные лыжи\n']

with open('users.csv', 'w', encoding='utf-8')as f:
    f.writelines(NAMES)

with open('hobby.csv', 'w', encoding='utf-8')as f:
    f.writelines(HOBBYS)

with open('users.csv', encoding='utf-8')as f_1, open('hobby.csv', encoding='utf-8')as f_2:
    f_1_l = len(f_1.readlines())
    f_2_l = len(f_2.readlines())
    f_1.seek(0)
    f_2.seek(0)
    mans = {}
    if f_1_l >= f_2_l:
        for i in range(f_2_l):
            mans[f_1.readline().strip()] = f_2.readline().strip()
        for i in range(f_2_l, f_1_l):
            mans[f_1.readline().strip()] = None
    else:
        sys.exit(1)
    mans = json.dumps(mans)

with open('users_hobbys.json', 'w+', encoding='utf-8') as f:
    f.write(mans)
    print(f.read())

with open('users_hobbys.json', 'r', encoding='utf-8') as f:
    mans = json.loads(f.read())
    print(mans)