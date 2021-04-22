def odd_nums(number):
    for el in range(1, number+1, 2):
        yield el


odd_to_15 = odd_nums(15)
print(odd_to_15)
# print(*odd_to_15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
# print(next(odd_to_15))

odd_numbers = (el for el in range(1, 16, 2))
print(odd_numbers)
print(*odd_numbers)
