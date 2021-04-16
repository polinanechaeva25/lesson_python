def thesaurus_adv(*args):
    names = {}
    for el in args:
        el = el.split()
        if names.get(el[1][0]):
            names[el[1][0]].append(' '.join(el))
        else:
            names[el[1][0]] = [' '.join(el)]
    my_names = names.copy()
    for key in my_names.keys():
        names[key] = {}
        for el in my_names[key]:
            if names[key].get(el[0]):
                names[key][el[0]].append(el)
            else:
                names[key][el[0]] = [el]
    return names


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))