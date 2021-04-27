import sys

NAMES = ['Иванов,Иван,Иванович\n', 'Петров,Петр,Петрович\n', 'Нечаева,Полина,Игоревна']
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
    with open('users_hobby.txt', 'w', encoding='utf-8') as f:
        if f_1_l >= f_2_l:
            for i in range(f_2_l):
                f.write(f'{f_1.readline().strip()}: {f_2.readline().strip()}\n')
            for i in range(f_2_l, f_1_l):
                f.write(f'{f_1.readline().strip()}: None\n')
        else:
            sys.exit(1)
