import numpy as np

class NumMatrix(object):
    def __init__(self, matrix):
        self.amount = [[0, ] * len(matrix[0]) for _ in range(len(matrix))]
        matrix = np.array(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.amount[i][j] = np.sum(matrix[:i+1, :j+1].flatten())
        # print(self.amount)
    def sumRegion(self, row1, col1, row2, col2):
        sum = self.amount[row2][col2]
        # print(sum)
        if col1:
            sum -= self.amount[row2][col1-1]
            # print(sum)
        if row1:
            sum -= self.amount[row1 - 1][col2]
            # print(sum)
        if col1 and row1:
            sum += self.amount[row1-1][col1-1]
            # print(sum)
        return sum


s = NumMatrix(
[
    [-4, -5]
])
print(s.sumRegion(0,0,0,1))