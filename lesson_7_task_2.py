import os
path = os.path.dirname(__file__)
with open('config.txt', encoding='utf-8') as f:
    content = f.read().splitlines()
    lvl = 0
    for el in content:
        if not el.index('|--') // 3 - lvl:
            if el.find('.py') != -1 or el.find('.html') != -1:
                os.path.join(path, el[el.index('|--') + 3:])
                try:
                    with open(el[el.index('|--') + 3:], 'x', encoding='utf-8') as f:
                        pass
                except FileExistsError as e:
                    print(e)
            else:
                path = os.path.join(path, el[el.index('|--') + 3:])
                if not os.path.exists(el[el.index('|--') + 3:]):
                    os.mkdir(el[el.index('|--') + 3:])
                os.chdir(path)
                lvl += 1
        elif el.index('|--') // 3 - lvl < 0:
            while el.index('|--') // 3 - lvl:
                path = os.path.join(path, '../')
                os.chdir(path)
                lvl -= 1
            if el.find('.py') != -1 or el.find('.html') != -1:
                os.path.join(path, el[elem.index('|--') + 3:])
                try:
                    with open(el[el.index('|--') + 3:], 'x', encoding='utf-8') as f:
                        pass
                except FileExistsError as e:
                    print(e)
            else:
                path = os.path.join(path, el[el.index('|--') + 3:])
                if not os.path.exists(el[el.index('|--') + 3:]):
                    os.mkdir(el[el.index('|--') + 3:])
                os.chdir(path)
                lvl += 1