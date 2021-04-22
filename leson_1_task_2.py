lst = []
for i in range(1, 1001):
    if i % 2 == 1:
        lst.append(i ** 3)


def multiple7(numbers):
    sum_numbers = 0
    for number in numbers:
        summ = 0
        number_round = number
        while number_round:
            summ += number_round % 10
            number_round = number_round // 10
        if summ % 7 == 0:
            sum_numbers += number
    return sum_numbers


result_1 = multiple7(lst)
print(result_1)
i = 0
while i < len(lst):
    lst[i] += 17
    i += 1
result_2 = multiple7(lst)
print(result_2)
