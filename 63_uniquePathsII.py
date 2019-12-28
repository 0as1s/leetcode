from functools import lru_cache

@lru_cache(10240)
def uniquePaths(m, n):
    if m == 0 or n == 0:
        return 0
    i = 1
    for j in range(max(m, n), m + n - 1):
        i *= j
    for j in range(2, min(m, n)):
        i /= j
    return int(i)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
            if obstacleGrid[0][0] == 1:
                return 0
            return 1
        if obstacleGrid[0][0] == 1:
            return 0
        total = uniquePaths(min(len(obstacleGrid), len(obstacleGrid[0])), max(len(obstacleGrid), len(obstacleGrid[0])))
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    x = len(obstacleGrid) - i
                    y = len(obstacleGrid[0]) - j
                    if i != 0:
                        total -= uniquePaths(min(x, y), max(x, y))
                    if j != 0:
                        total -= uniquePaths(min(x, y), max(x, y))
        return max(total, 0)

s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
print(s.uniquePathsWithObstacles([[0,0],[1,0]]))
print(s.uniquePathsWithObstacles([
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,0],
    [0,0,1,0],
    [0,0,0,0]
]))