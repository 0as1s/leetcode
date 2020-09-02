class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nums = 0
        visited = set()
        from queue import deque
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    if grid[i][j] == 1:
                        continue
                    q = deque()
                    q.append((i, j))
                    flag=True
                    while q:
                        cur = q.popleft()
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            next_i = cur[0] + x
                            next_j = cur[1] + y
                            if next_i < 0 or next_i >= len(grid) or next_j < 0 or next_j >= len(grid[0]):
                                flag = False
                                continue
                            else:
                                if (next_i, next_j) not in visited:
                                    visited.add((next_i, next_j))
                                    if grid[next_i][next_j] == 0:
                                        q.append((next_i, next_j))
                    if flag:
                        nums += 1
        return nums
                            
