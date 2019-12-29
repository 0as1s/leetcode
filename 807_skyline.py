from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        left = [0] * len(grid)
        up = [0] * len(grid[0])
        for i in range(len(grid)):
            left[i] = max(grid[i])
        for j in range(len(grid[0])):
            m = -float("Inf")
            for i in range(len(grid)):
                m = max(m, grid[i][j])
            up[j] = m
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(left[i], up[j]) - grid[i][j]
        return total

grid = [[0]]
print(Solution().maxIncreaseKeepingSkyline(grid))