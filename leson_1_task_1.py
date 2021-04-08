duration = int(input('Введите продолжительность времени в секундах: '))
if duration < 60:
    print(f'{duration} sec')
elif duration < 3600:
    print(f'{duration // 60} min {duration % 60} sec')
elif duration < 3600*60:
    print(f'{duration // 3600} hours {duration % 3600 // 60} min {duration % 60} sec')
elif duration < 24*3600*60:
    print(f'{duration // 24 // 3600} days {duration // 3600 % 24} hours {duration % 3600 //60} min {duration % 60} sec')
