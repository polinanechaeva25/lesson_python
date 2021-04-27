import sys

# Для работы через терминал введите в соответствующем порядке название файла имен, название файла хобби,
# назание итогового файла
NAMES = ['Иванов,Иван,Иванович\n', 'Петров,Петр,Петрович\n', 'Нечаева,Полина,Игоревна']
HOBBYS = ['скалолазание,охота\n', 'горные лыжи\n']

with open(sys.argv[1], 'w', encoding='utf-8')as f:
    f.writelines(NAMES)

with open(sys.argv[2], 'w', encoding='utf-8')as f:
    f.writelines(HOBBYS)

with open(sys.argv[1], encoding='utf-8')as f_1, open(sys.argv[2], encoding='utf-8')as f_2:
    f_1_l = len(f_1.readlines())
    f_2_l = len(f_2.readlines())
    f_1.seek(0)
    f_2.seek(0)
    with open(sys.argv[3], 'w', encoding='utf-8') as f:
        if f_1_l >= f_2_l:
            for i in range(f_2_l):
                f.write(f'{f_1.readline().strip()}: {f_2.readline().strip()}\n')
            for i in range(f_2_l, f_1_l):
                f.write(f'{f_1.readline().strip()}: None\n')
        else:
            sys.exit(1)