class Solution(object):
    def tra(self, cur, used):
        if not (0 <= cur[0] < len(self.grid) and 0 <= cur[1] < len(self.grid[0])):
            return
        if cur in self.blocked:
            return
        if cur in used:
            return
        used = set(used)
        used.add(cur)
        if cur == self.end and len(used) == self.total:
            self.count += 1
            return
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in dirs:
            self.tra((cur[0]+d[0], cur[1]+d[1]), used)



    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.count = 0
        self.grid = grid
        self.blocked = set()
        start = None
        self.end = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    self.end = (i, j)
                if grid[i][j] == -1:
                    self.blocked.add((i, j))
        self.total = len(grid) * len(grid[0]) - len(self.blocked)
        self.tra(start, set())
        return self.count


s = Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0],[0,0,0,2]]))
s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
s.uniquePathsIII([[0,1],[2,0]])

# from functools import lru_cache
# class Solution:
#     def uniquePathsIII(self, grid):
#         R, C = len(grid), len(grid[0])
#
#         def code(r, c):
#             return 1 << (r * C + c)
#
#         def nei***ors(r, c):
#             for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
#                 if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
#                     yield nr, nc
#
#         target = 0
#         for r, row in enumerate(grid):
#             for c, val in enumerate(row):
#                 if val % 2 == 0:
#                     target |= code(r, c)
#
#                 if val == 1:
#                     sr, sc = r, c
#                 if val == 2:
#                     tr, tc = r, c
#
#         @lru_cache(None)
#         def dp(r, c, todo):
#             if r == tr and c == tc:
#                 return +(todo == 0)
#
#             ans = 0
#             for nr, nc in nei***ors(r, c):
#                 if todo & code(nr, nc):
#                     ans += dp(nr, nc, todo ^ code(nr, nc))
#             return ans
#
#         return dp(sr, sc, target)
# 使用lru_cache(None) 实现python的记忆化
# 使用位操作记录剩下要访问的位置