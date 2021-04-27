with open('nginx_logs.txt', 'r', encoding='utf=8') as f:
    ip = []
    for line in f:
        part_1 = line.split(' - -')
        part_2 = part_1[1].split('"')[1].split(' /')
        part_3 = part_2[1].split(' HTTP/')
        content = part_1[0], part_2[0], part_3[0]
        ip.append(part_1[0])

with open('nginx_logs.txt', 'r', encoding='utf=8') as f:
    max = 0
    name_max = None
    for line in f:
        part_1 = line.split(' - -')[0]
        if max < ip.count(part_1):
            max = ip.count(part_1)
            name_max = part_1 = line.split(' - -')[0]
    print(max, name_max)
