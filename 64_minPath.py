class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i-1][j]+grid[i][j], grid[i][j-1]+grid[i][j])
        return grid[-1][-1]
