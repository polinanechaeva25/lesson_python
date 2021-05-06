class Stationery:
    title = 'пейзаж'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Начало записи')


class Pencil(Stationery):

    def draw(self):
        print('Создается набросок')


class Handle(Stationery):

    def draw(self):
        print('Выделяем главное')


item_1 = Stationery()
print(item_1.title)
item_1.draw()
item_2 = Pen()
print(item_2.title)
item_2.draw()
item_3 = Pencil()
print(item_3.title)
item_3.draw()
item_4 = Handle()
print(item_4.title)
item_4.draw()
