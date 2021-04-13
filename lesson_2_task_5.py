prices = [57.08, 46.5, 97, 32.7, 84.57, 21.34, 66.02, 15.15, 78.09, 114.46]

# Пункт А
lst = []
for price in prices:
    a = str(int((price - int(price)) * 100))
    if len(a) == 1:
        a = '0' + a
    lst.append((str(int(price)) + ' руб ' + a + ' коп'))
print(' ,'.join(lst))

# Пункт B
print(prices)
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

# Пункты C, D
new_prices = sorted(prices, reverse=True)
print(new_prices)
print(new_prices[:5])
print(id(new_prices))
