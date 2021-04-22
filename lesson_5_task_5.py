src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq = set()
replay = set()
for el in src:
    if el in replay:
        uniq.discard(el)
    else:
        uniq.add(el)
        replay.add(el)
result = [el for el in src if el in uniq]
print(result)
