from queue import deque

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        q.append(-1)
        count = 0
        while q:
            cur = q.popleft()
            if cur == -1:
                if not q:
                    break
                count += 1
                q.append(-1)
                continue
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                n = (cur[0]+i, cur[1]+j)
                if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]):
                    if grid[n[0]][n[1]] == 1:
                        grid[n[0]][n[1]] = 2
                        q.append((n[0], n[1]))
        for i in grid:
            for j in i:
                if j == 1:
                    return -1
        return count

s = Solution()
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0, 2]]))