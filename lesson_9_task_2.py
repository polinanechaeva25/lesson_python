class Road:
    # масса асфальта (кг) для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см:
    m = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, thickness):
        mass = self._length * self._width * self.m * thickness
        mass = f'{round(mass/1000)} т'
        return mass


road_1 = Road(5000, 20)
print(road_1.calc_mass(5))
