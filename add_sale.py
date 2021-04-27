import sys
with open('bakery.csv', 'a', encoding='utf-8') as f:
    # Делаю все элементы одной длины
    f.write('\n' + sys.argv[1] + (9 - len(sys.argv[1]))*' ')
