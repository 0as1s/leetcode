def minCost(self, grid: List[List[int]]) -> int:
	if not grid or not grid[0]:
		return True

	m, n = len(grid), len(grid[0])

	directions = [[0,0],[0,1],[0,-1],[1,0],[-1,0]]

	q = deque([(0,0,0)])
	visit = set()
	visit.add((0,0))

	while q:
		cx, cy, dis = q.popleft()

		if cx == m-1 and cy == n-1:
			return dis

		visit.add((cx, cy))

		for i in range(1,5):
			nx = cx + directions[i][0]
			ny = cy + directions[i][1]
			cost = 1 if grid[cx][cy] != i else 0
			if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visit:
				if cost == 1:
					q.append((nx, ny, dis+1))
				else:
					q.appendleft((nx, ny, dis))

	return -1

# class Solution(object):
#     def minCost(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         dd = {
#             1: (0, 1),
#             2: (0, -1),
#             3: (1, 0),
#             4: (-1, 0)
#         }
#         current = set([(0, 0)])
#         cur = (0, 0)
#         h = len(grid)
#         l = len(grid[0])
#         count = 0
#         used = set()
#         while True:
#             x, y = cur
#             if x == h-1 and y == l-1:
#                 return count
#             dx, dy = dd[grid[x][y]]
#             nx, ny = x + dx, y + dy
#             if (nx, ny) not in used and 0 <= nx < h and 0 <= ny < l:
#                 if nx == h-1 and ny == l-1:
#                     return count
#                 current.add((nx, ny))
#                 used.add((nx, ny))
#                 cur = (nx, ny)
#             else:
#                 break
#         while True:
#             count += 1
#             new_current = set()
#             for cur in current:
#                 x, y = cur
#                 for dx, dy in dd.values():
#                     nx, ny = x + dx, y + dy
#                     if (nx, ny) not in used and 0 <= nx < h and 0 <= ny < l:
#                         if nx == h-1 and ny == l-1:
#                             return count
#                         used.add((nx, ny))
#                         new_current.add((nx, ny))
#                         ddx, ddy = dd[grid[nx][ny]]
#                         nnx, nny = nx + ddx, ny + ddy
#                         while (nnx, nny) not in used and 0 <= nnx < h and 0 <= nny < l:
#                             if nnx == h-1 and nny == l-1:
#                                 return count                            
#                             #used.add((nnx, nny))
#                             new_current.add((nnx, nny))
#                             ddx, ddy = dd[grid[nnx][nny]]
#                             nnx, nny = nx + ddx, ny + ddy
#             current = new_current