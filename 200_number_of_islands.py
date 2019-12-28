class Solution(object):

    def numIslands(self, grid):
        if not grid:
            return 0
        total = 0
        visit = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                if grid[i][j] == '1' and not visit[i][j]:
                    total += 1
                    q = []
                    q.append((i, j))
                    while q:
                        cur = q[0]
                        if cur[0] > 0 and grid[cur[0] - 1][cur[1]] == '1' and not visit[cur[0] - 1][cur[1]]:
                            q.append((cur[0] - 1, cur[1]))
                            visit[cur[0] - 1][cur[1]] = 1
                        if cur[0] < len(grid) - 1 and grid[cur[0] + 1][cur[1]] == '1' and not visit[cur[0] + 1][cur[1]]:
                            q.append((cur[0] + 1, cur[1]))
                            visit[cur[0] + 1][cur[1]] = 1
                        if cur[1] > 0 and grid[cur[0]][cur[1] - 1] == '1' and not visit[cur[0]][cur[1] - 1]:
                            q.append((cur[0], cur[1] - 1))
                            visit[cur[0]][cur[1] - 1] = 1
                        if cur[1] < len(grid[0]) - 1 and grid[cur[0]][cur[1] + 1] == '1' and not visit[cur[0]][cur[1] + 1]:
                            q.append((cur[0], cur[1] + 1))
                            visit[cur[0]][cur[1] + 1] = 1
                        del(q[0])
        return total

nums = [
    "11000", "11000", "00100", "00011",
]
# nums = ["101000"]
s = Solution()
print s.numIslands(nums)
