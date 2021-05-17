class CheckNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


test_lst = []
i = 1
while True:
    data_check = input(f'Введите {i} число списка или введите "stop" , чтобы остановиться: ')
    if data_check == 'stop':
        break
    try:
        for el in data_check:
            if el not in str([element for element in range(10)]) and el != '.':
                raise CheckNumber('Введено не число!')
    except CheckNumber as err:
        print(err)
    else:
        test_lst.append(round(float(data_check), 2))
        i += 1
print(test_lst)
