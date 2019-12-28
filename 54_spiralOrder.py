class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        r = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur = (0, -1)
        i = 0
        while len(r) != (len(matrix) * len(matrix[0])):

            x = cur[0] + dirs[i][0]
            y = cur[1] + dirs[i][1]
            if not 0<= x < len(matrix) or not 0 <= y <len(matrix[0]) or matrix[x][y] == float("Inf"):
                i = (i+1) % 4
                continue
            r.append(matrix[x][y])
            matrix[x][y] = float("Inf")
            cur = (x, y)
        return r


s = Solution()
print(s.spiralOrder(
[[2,5],[8,4],[0,-1]]))