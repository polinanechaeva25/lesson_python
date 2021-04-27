import sys
with open('bakery.csv', encoding='utf-8') as f:
    print(f.readlines())
    # if len(sys.argv) == 1:
    #     print(f.read())
    # elif len(sys.argv) == 2:
    #     print(*f.readlines()[int(sys.argv[1]):], sep='')
    # elif len(sys.argv) == 3:
    #     print(*f.readlines()[int(sys.argv[1]):int(sys.argv[2]) + 1], sep='')