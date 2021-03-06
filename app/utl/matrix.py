class IncompatibleMatricesError(ValueError):
    pass

class Matrix:

    @staticmethod
    def multiply(m1, m2):
        print(m1)
        print(m2)
        if len(list(m1[0])) != len(list(m2)):
            raise IncompatibleMatricesError('Matrices cannot be multiplied!')
            return -1
        result = []
        for y in range(len(m1)):
            row = []
            for x in range(len(m2[0])):
                v1 = m1[y][:]
                v2 = [i[x] for i in m2]
                row.append(sum([float(v1[i]) * float(v2[i]) for i in range(len(v1))]))
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
        print(m)
        if len(m) == 0:
            for x in values:
                m.append([x])
        elif len(m) == len(values):
            for x in range(len(values)):
                m[x].append(values[x])
        else:
            raise IncompatibleMatricesError('Column cannot be added to matrix')
        return m
    
    @staticmethod
    def read(matrixstr):
        if(matrixstr == []):
            return []
        rows = matrixstr.split('\\')
        return list(map(lambda x: x.split('&'), rows))

    @staticmethod
    def toString(matrix):
        rows = list(map(lambda x: '&'.join(map(str, x)), matrix))
        return '\\'.join(rows)