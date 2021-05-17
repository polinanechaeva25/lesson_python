class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        return ComplexNumber(self.number + other.number)

    def __mul__(self, other):
        return ComplexNumber(self.number * other.number)


n_1 = ComplexNumber(2 + 3j)
n_2 = ComplexNumber(-5 - 7j)
print(n_1 * n_2)
print(n_1 + n_2)
