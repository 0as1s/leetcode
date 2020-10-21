class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [[0]*n for _ in range(n)]
        d = {
            0:(0, 1),
            1:(1, 0),
            2:(0, -1),
            3:(-1, 0)
        }
        x, y = 0, 0
        dd = 0
        for i in range(n*n):
            m[x][y] = (i+1)
            if i == n*n - 1:
                break
            while True:
                xx, yy = x + d[dd][0], y + d[dd][1]
                if 0 <= xx < n and 0 <= yy < n and m[xx][yy] == 0:
                    break
                dd = (dd + 1) % 4
            if 0 <= xx < n and 0 <= yy < n and m[xx][yy] == 0:
                x, y = xx, yy
        return m

s = Solution()
print(s.generateMatrix(3))