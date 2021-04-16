def thesaurus(*args):
    names = {}
    for el in args:
        if names.get(el[0]):
            names[el[0]].append(el)
        else:
            names[el[0]] = [el]
    return names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
