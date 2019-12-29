from typing import List
from queue import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # left = 0
        m = 0
        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    s.add((i, j))
        while s:
            q = deque()
            q.append(s.pop())
            square = 1
            while q:
                cur = q.popleft()
                for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) in s:
                        q.append((x, y))
                        s.remove((x, y))
                        square += 1
            # print(left)
            # print(s)
            m = max(square, m)
            if m >= len(s):
                return m
        return 0

M = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# M = [[]]
# M = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
# M = [[0,1],[1,1]]
s = Solution()
print(s.maxAreaOfIsland(M))