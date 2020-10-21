class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[1] * N for _ in range(N)]
        for m in mines:
            grid[m[0]][m[1]] = 0
        m = grid
        left = [[0] * N for _ in range(N)]
        right = [[0] * N for _ in range(N)]
        up = [[0] * N for _ in range(N)]
        down = [[0] * N for _ in range(N)]
        for i in range(len(m)):
            l = -1
            for j in range(len(m[0])):
                if m[i][j] == 0:
                    l = j
                else:
                    left[i][j] = j - l
        for i in range(len(m)):
            r = len(m[0])
            for j in range(len(m[0])-1, -1, -1):
                if m[i][j] == 0:
                    r = j
                else:
                    right[i][j] = r - j
        for j in range(len(m[0])):
            u = -1
            for i in range(len(m)):
                if m[i][j] == 0:
                    u = i
                else:
                    up[i][j] = i-u
        for j in range(len(m[0])):
            d = len(m)
            for i in range(len(m)-1, -1, -1):
                if m[i][j] == 0:
                    d = i
                else:
                    down[i][j] = d - i
        r = 0    
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 1:
                    r = max(r, min(left[i][j], right[i][j], up[i][j], down[i][j]))
        return r