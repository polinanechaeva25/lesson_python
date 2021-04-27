with open('nginx_logs.txt', 'r', encoding='utf=8') as f:
    my_lst = []
    for line in f:
        part_1 = line.split(' - -')
        part_2 = part_1[1].split('"')[1].split(' /')
        part_3 = f'/{part_2[1].split(" HTTP/")[0]}'
        content = part_1[0], part_2[0], part_3
        my_lst.append(content)
print(*my_lst, sep='\n')