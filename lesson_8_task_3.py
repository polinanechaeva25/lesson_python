def type_logger(callback):
    def wrapper(*args):
        for i in args:
            tp = type(i)
            print(f'{i}: {tp}', end=', ')
        result = callback(*args)
        print(f'тип значения функции: {type(result)}')
        return result
    return wrapper

@type_logger
def calc_cube(*x):
    array = []
    for i in x:
      array.append(i ** 3)
    return array

a = calc_cube(5, 4, 6)
print()
print(a)

