def num_translate(key):
    words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if words.get(key.lower()):
        if key[0].isupper():
            return words[key.lower()].title()
        else:
            return words[key]


print(num_translate(input('Введиче число от 0 до 10 на английском: ')))
