from collections import defaultdict


class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.result = dict()
        self.start = defaultdict(set)
        self.end = defaultdict(set)

    def sumRegion(self, row1, col1, row2, col2):
        if (row1, col1, row2, col2) in self.result.keys():
            return self.result[(row1, col1, row2, col2)]

        for k1 in self.start[(row1, col1)]:
            if k1[2] == row2:
                k2 = (row1, k1[3] + 1, row2, col2)
                if k2 not in self.end[(row2, col2)]:
                    continue
                else:
                    result = self.result[k1] + self.result[k2]
                    self.result[(row1, col1, row2, col2)] = result
                    self.start[(row1, col1)].add((row1, col1, row2, col2))
                    self.end[(row2, col2)].add((row1, col1, row2, col2))
                    return result
            if k1[3] == col2:
                k2 = (k1[2] + 1, col1, row2, col2)
                if k2 not in self.end[(row2, col2)]:
                    continue
                else:
                    result = self.result[k1] + self.result[k2]
                    self.result[(row1, col1, row2, col2)] = result
                    self.start[(row1, col1)].add((row1, col1, row2, col2))
                    self.end[(row2, col2)].add((row1, col1, row2, col2))
                    return result

        result = 0
        for i in xrange(row1, row2 + 1):
            for j in xrange(col1, col2 + 1):
                result += self.matrix[i][j]
            # result += sum(self.matrix[i][col1, col2 + 1])
        self.result[(row1, col1, row2, col2)] = result
        self.start[(row1, col1)].add((row1, col1, row2, col2))
        self.end[(row2, col2)].add((row1, col1, row2, col2))
        return result


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]


s = NumMatrix(matrix)
print s.sumRegion(2, 1, 3, 3)
print s.sumRegion(4, 1, 4, 3)
print s.sumRegion(2, 1, 4, 3)
print s.sumRegion(1, 1, 2, 2)
print s.sumRegion(1, 2, 2, 4)
