class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


numerator = input('Введите делимое число: ')
try:
    denominator = input('Введите делитель: ')
    if float(denominator) == 0:
        raise ZeroDiv('Попытка деления на ноль')
except ZeroDiv as err:
    print(err)
else:
    result = float(numerator) / float(denominator)
    print(round(result, 2))
finally:
    print('Работа завершена')
