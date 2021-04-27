import sys
with open('bakery.csv', 'r+', encoding='utf-8') as f:
    n = int(sys.argv[1])
    f.seek(2 + 11 * (n - 1))
    f.write(sys.argv[2] + (9 - len(sys.argv[2]))*' ' + '\n')