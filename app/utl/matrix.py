class IncompatibleMatricesError(ValueError):
    pass

class Matrix:

    @staticmethod
    def multiply(m1, m2):
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

    @staticmethod
    def add_row(m, values):
        if len(m) == 0:
            m.append(values)
        elif len(m[0]) == len(values):
            m.append(values)
        else:
            raise IncompatibleMatricesError('Row cannot be added to matrix')
    
    @staticmethod
    def add_column(m, values):
        if len(m) == 0:
            for x in values:
                m.append([x])
        elif len(m) == len(values):
            for x in range(len(values)):
                m[x].append(values[x])
        else:
            raise IncompatibleMatricesError('Column cannot be added to matrix')
    
    @staticmethod
    def read(matrixstr):
        rows = matrixstr.split('\\')
        return map(lambda x: x.split('&'), rows)

    @staticmethod
    def toString(matrix):
        rows = map(lambda x: '&'.join(map(str, x)), matrix)
        return '\\'.join(rows)