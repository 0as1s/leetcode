class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for ii in range(len(matrix)):
                        if matrix[ii][j] != 0:
                            matrix[ii][j] = float("Inf")
                    for jj in range(len(matrix[0])):
                        if matrix[i][jj] != 0:
                            matrix[i][jj] = float("Inf")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float("Inf"):
                    matrix[i][j] = 0

