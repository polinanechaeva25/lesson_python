weather_now = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst = []
for indx in range(len(weather_now)):
    for el in weather_now[indx]:
        if weather_now[indx].find('.') == -1:
            for i in range(10):
                if el == str(i):
                    lst.append(weather_now[indx])
lst = list(set(lst))
for element in lst:
    for ind in range(len(weather_now)):
        if weather_now[ind] == element:
            if len(element) == 1:
                weather_now[ind] = '0' + weather_now[ind]
            elif len(element) == 2 and (element[0] == '+' or element[0] == '-'):
                weather_now[ind] = weather_now[ind][0] + '0' + weather_now[ind][1]
            weather_now.insert(ind + 1, '"')
            weather_now.insert(ind, '"')
            break
print(weather_now)
a = weather_now.count('"')
for ind in range(len(weather_now) - a):
    if weather_now[ind] == '"':
        weather_now[ind] += weather_now.pop(ind + 1) + weather_now.pop(ind + 1)
print(' '.join(weather_now))
