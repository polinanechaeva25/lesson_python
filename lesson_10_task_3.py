class Cell:

    def __init__(self, volume):
        self.volume = volume

    def __str__(self):
        return f'{self.volume}'

    def __add__(self, other):
        return Cell(self.volume + other.volume)

    def __sub__(self, other):
        result = self.volume - other.volume
        if result > 0:
            return Cell(result)
        else:
            return 'Разность количества ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        result = self.volume * other.volume
        return Cell(result)

    def __floordiv__(self, other):
        result = self.volume // other.volume
        return Cell(result)

    def make_order(self, lot):
        result = ''
        for _ in range(self.volume // lot):
            result += '*' * lot + '\n'
        result += '*' * (self.volume % lot)
        return result


cell_1 = Cell(14)
cell_2 = Cell(5)
print(cell_2 + cell_1)
print(cell_2 - cell_1)
print(cell_1 - cell_2)
print(cell_2 * cell_1)
print(cell_1 // cell_2)
print(cell_1.make_order(4))