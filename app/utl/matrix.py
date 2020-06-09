class IncompatibleMatricesError(ValueError):
    pass

class Matrix:

    value = None

    def __init__(self, matrix):
        self.value = matrix

    def multiply(matrix1, matrix2):
        m1 = matrix1.value
        m2 = matrix2.value
        if len(m1[0]) != len(m2):
            raise IncompatibleMatricesError('Matrices cannot be multiplied!')
            return -1
        result = []
        for y in range(len(m1)):
            row = []
            for x in range(len(m2[0])):
                v1 = m1[x][:]
                v2 = [i[x] for i in m2]
                row.append(sum([v1[i] * v2[i] for i in range(len(v1))]))
            result.append(row)
        return result

    def add_row(self, values):
        if len(self.value) == 0:
            self.value.append(values)
        elif len(self.value[0]) == len(values):
            self.value.append(values)
        else:
            raise IncompatibleMatricesError('Row cannot be added to matrix')
    
    def add_column(self, values):
        if len(self.value) == 0:
            for x in values:
                self.value.append([x])
        elif len(self.value) == len(values):
            for x in range(len(values)):
                self.value[x].append(values[x])
        else:
            raise IncompatibleMatricesError('Column cannot be added to matrix')