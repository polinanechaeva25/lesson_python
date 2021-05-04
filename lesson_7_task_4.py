import os
import random

# Для создания рандомных файлов  в папке "some_data"

# folder = 'some_data'
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(40):
#    f_name = ''.join(random.sample(letters, random.randint(0, 5)))
#    f_content = bytes(random.randint(0, 255)for _ in range(random.randrange(100)))
#    with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#        f.write(f_content)

size = {}
wt = []
for el in os.scandir('some_data'):
    wt.append(os.stat(el).st_size)
for i in [10, 100, 10 ** 3, 10 ** 4, 10 ** 5]:
    counter = 1
    for el in wt:
        if i / 10 < el < i:
            size[i] = counter
            counter += 1
print(size)
