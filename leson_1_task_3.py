my_percent = int(input('Введите количество процентов от 0 до 20: '))
if 0 > my_percent > 20:
    my_percent = int(input('Введено неверное число, введите число от 0 до 20: '))
elif my_percent == 0 or my_percent > 5:
    perсent = 'процентов'
elif my_percent == 1:
    perсent = "процент"
else:
    perсent = "процента"
print(my_percent, perсent)
