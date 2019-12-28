class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l // 2):
            for j in range(i, l-i-1):
                matrix[i][j], matrix[j][l-i-1], matrix[l-i-1][l-j-1], matrix[l-j-1][i] = matrix[l-j-1][i], matrix[i][j], matrix[j][l-i-1], matrix[l-i-1][l-j-1]


s = Solution()
s.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], )
s.rotate([1,])