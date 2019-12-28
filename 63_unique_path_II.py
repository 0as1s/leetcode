class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):

        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        ways = [[0 for i in range(len(obstacleGrid[0]))]
                for i in range(len(obstacleGrid))]
        ways[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1, len(obstacleGrid[0])):
            ways[0][i] = ways[0][i - 1] if not obstacleGrid[0][i - 1] else 0
            if obstacleGrid[0][i]:
                ways[0][i] = 0
        for i in range(1, len(obstacleGrid)):
            ways[i][0] = ways[i - 1][0] if not obstacleGrid[i - 1][0] else 0
            if obstacleGrid[i][0]:
                ways[i][0] = 0
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                ways[i][j] = 0 if obstacleGrid[i][
                    j] else ways[i - 1][j] + ways[i][j - 1]
        return ways[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

matrix = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
matrix = [[1]]
matrix = [[0, 1, 0]]
matrix = [[0], [1], [0]]

s = Solution()
print s.uniquePathsWithObstacles(matrix)
