weather_now = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst = []
for indx in range(len(weather_now)):
    for el in weather_now[indx]:
        if weather_now[indx].find('.') == -1:
            for i in range(10):
                if el == str(i):
                    lst.append(indx)
lst = list(set(lst))
for element in lst:
    if len(weather_now[element]) == 1:
        weather_now[element] = '0' + weather_now[element]
    elif len(weather_now[element]) == 2 and (weather_now[element][0] == '+' or weather_now[element][0] == '-'):
        weather_now[element] = weather_now[element][0] + '0' + weather_now[element][1]
weath_n = weather_now.copy()
for element in lst:
    for ind in range(len(weath_n)):
        if weath_n[ind] == weather_now[element]:
            weath_n.insert(ind + 1, '"')
            weath_n.insert(ind, '"')
            break
print(weath_n)
a = weath_n.count('"')
for ind in range(len(weath_n) - a):
    if weath_n[ind] == '"':
        weath_n[ind] += weath_n.pop(ind + 1) + weath_n.pop(ind + 1)
print(' '.join(weath_n))
