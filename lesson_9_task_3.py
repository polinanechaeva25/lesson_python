class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        income = {"wage": wage, "bonus": bonus}
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        tot_income = 0
        for val in self._income.values():
            tot_income += val
        return tot_income


person_1 = Position('Polina', 'Nechaeva', 'engineer', 45000, 3000)
print(person_1.name)
print(person_1.surname)
print(person_1.position)
print(person_1._income)
person_1.get_full_name()
print(person_1.get_total_income())
