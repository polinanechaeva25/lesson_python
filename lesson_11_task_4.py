import time


class Warehouse:
    check = {}
    place = {}

    def __init__(self, name):
        try:
            if type(name) != str:
                raise ValueError(f"Названение объекта введено некорректно: {name}")
        except ValueError as err:
            print(err)
        else:
            self.name = name

    def accept(self, sum):
        try:
            if type(sum) != int:
                raise ValueError(f'Неверное значение входных данных: {sum}')
        except ValueError as err:
            return err
        else:
            if self.check.get(self.name):
                self.check[self.name] += sum
            else:
                self.check[self.name] = sum
            return self.check

    def transfer(self, sum, name_place, store):
        try:
            if type(sum) != int:
                raise ValueError(f'Неверное значение входных данных: {sum}')
        except ValueError as err:
            return err
        else:
            if store.get(self.name):
                if sum <= store[self.name]:
                    store[self.name] -= sum
                    if self.place.get(name_place):
                        if self.place[name_place].get(self.name):
                            self.place[name_place][self.name] += sum
                        else:
                            self.place[name_place][self.name] = sum
                    else:
                        self.place[name_place] = {self.name: sum}
                    return self.place
                else:
                    return 'Недостаточно товара на складе'
            else:
                return 'Товар отсутствует на складе'


class OfficeEquipment:
    def __init__(self, name, activ=True):
        try:
            if type(name) != str:
                raise ValueError(f"Названение объекта введено некорректно: {name}")
            else:
                self.name = name
            if not type(activ) == bool:
                raise ValueError(f"Неверный тип данных переменной объекта {self.name}")
        except ValueError as err:
            print(err)
        else:
            self.activ = activ


class Printer(OfficeEquipment):
    def __init__(self, name, picture=False, color=True, activ=True):
        super().__init__(name, activ)
        try:
            if type(color) != bool or type(picture) != bool:
                raise ValueError(f"Неверный тип данных переменной объекта {self.name}")
        except ValueError as err:
            print(err)
        else:
            self.color = color
            self.picture = picture

    def __str__(self):
        return f'{Printer.__name__} {self.name}'

    def print_out(self, txt):
        try:
            if not self.activ:
                raise Exception(f'Устройство {self.name} выключено')
        except Exception as err:
            return err
        else:
            if not self.picture:
                return f'{txt}'
            elif not self.color:
                return f'печать ч/б изображения: {txt}'
            else:
                return f'печать цветного изображения: {txt}'


class Scanner(OfficeEquipment):
    def __init__(self, name, quality=5, activ=True):
        super().__init__(name, activ)
        try:
            if type(quality) != int:
                raise ValueError(f'Неверное значение входных данных объекта {self.name}: "качество изображения" ')
        except ValueError as err:
            print(err)
        else:
            self.quality = quality

    def __str__(self):
        return f'{Scanner.__name__} {self.name}'

    def scan(self, words):
        try:
            if not self.activ:
                raise Exception(f'Устройство {self.name} выключено')
        except Exception as err:
            return err
        else:
            # чем выше качество изображения, тем дольше проходит сканирование
            time.sleep(self.quality)
            return f'{words}'


class Copier(OfficeEquipment):
    def __init__(self, name, copies=1, doc=True, activ=True):
        super().__init__(name, activ)
        try:
            if type(doc) != bool:
                raise ValueError(f"Неверный тип данных переменной объекта {self.name}")
            if type(copies) != int:
                raise ValueError(f'Неверное значение входных данных объекта {self.name}: "количество копий"')
        except ValueError as err:
            print(err)
        else:
            self.copies = copies
            self.doc = doc

    def __str__(self):
        return f'{Copier.__name__} {self.name}'

    def make_a_copy(self, txt):
        try:
            if not self.activ:
                raise Exception(f'Устройство {self.name} выключено')
        except Exception as err:
            return err
        else:
            if self.doc:
                return f'{txt}\n' * self.copies
            else:
                return f'создано {self.copies} копий изображения "{txt}"'


printer_1 = Printer('HP', True)
printer_2 = Printer('Asus', activ=False)
printer_3 = Printer(4)
print(printer_2.print_out('some_txt'))
print(printer_1.print_out('Sun'))
print()

scanner_1 = Scanner('Lenovo', '7', False)
scanner_2 = Scanner('Dell', 5, [True])
scanner_3 = Scanner('Sony', 2)
print(scanner_3.scan('Доброго времени суток'))
print()

copier_1 = Copier('Samsung', 2, 'False')
copier_2 = Copier('Acer', [8])
copier_3 = Copier('Canon', 3)
copier_4 = Copier('Fujifilm', 2, False)
print(copier_3.make_a_copy('Здравствуйте'))
print(copier_4.make_a_copy('Водопад'))
print()

ob_1 = Warehouse(str(printer_1))
entrance_1 = ob_1.accept('4')
print(entrance_1)
entrance_1 = ob_1.accept(4)
print(entrance_1)
print()

ob_2 = Warehouse(str(scanner_3))
entrance_2 = ob_2.accept(5)
print(entrance_2)
print(ob_2.transfer(6, 'Главный корпус', entrance_2))
print(ob_2.transfer(5, 'Главный корпус', entrance_2))
print(entrance_2)
print()

ob_3 = Warehouse(str(copier_3))
print(ob_2.transfer(6, 'Главный корпус', entrance_2))
entrance_3 = ob_3.accept(2)
print(entrance_3)
print(ob_3.transfer(1, 'Второе подразделение', entrance_3))
print(entrance_3)
