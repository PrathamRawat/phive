class Matrix:

    value = None

    def __init__(self):
        self.value = []

    def multiply(m1, m2):
        if len(m1[0]) != len(m2):
            print('Matrices cannot be multiplied!')
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