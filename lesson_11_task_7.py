import re


class ComplexNumber:
    def __init__(self, number):
        self.number = number
        pattern = re.compile(r'([-+]\d)([-+]\d)i')
        result = pattern.finditer(self.number)
        for el in result:
            self.valid = float(el.group(1))
            self.imaginary = float(el.group(2))

    def __str__(self):
        return self.number

    def __add__(self, other):
        valid = self.valid + other.valid
        imaginary = self.imaginary + other.imaginary
        if valid == 0:
            return f'{imaginary}i'
        elif imaginary == 0:
            return valid
        elif imaginary < 0:
            return f'{valid}{imaginary}i'
        else:
            return f'{valid}+{imaginary}i'

    def __mul__(self, other):
        valid = self.valid * other.valid - other.imaginary * self.imaginary
        imaginary = self.valid * other.imaginary + other.valid * self.imaginary
        if valid == 0:
            return f'{imaginary}i'
        elif imaginary == 0:
            return valid
        elif imaginary < 0:
            return f'{valid}{imaginary}i'
        else:
            return f'{valid}+{imaginary}i'


n_1 = ComplexNumber('+2+3i')
n_2 = ComplexNumber('+5-7i')
n_3 = ComplexNumber('-5+9i')
n_4 = ComplexNumber('-5-7i')
print(n_3 + n_2)
print(n_1 * n_4)
