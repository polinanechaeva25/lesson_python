class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        string = ''
        for el in self.lst:
            for sb in el:
                string += f'{sb} '
            string += '\n'
        return string

    def __add__(self, other):
        matrix = []
        for ind in range(len(self.lst)):
            matrix.append([])
            for index in range(len(self.lst[ind])):
                matrix[ind].append(self.lst[ind][index]+other.lst[ind][index])
        return Matrix(matrix)


mat_1 = Matrix([[31, 22], [37, 43], [51, 86]])
print(mat_1)
mat_2 = Matrix([[1, 2], [4, 5], [1, 0]])
print(mat_1 + mat_2)
