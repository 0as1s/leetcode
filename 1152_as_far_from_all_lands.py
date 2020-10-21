from queue import deque
class Solution(object):
    def maxDistance(self, grid):
        
        # number of rows
        rows = len(grid)
        
        # number of columns
        cols = len(grid[0])
        
        # direction vectors
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        
        # queue for BFS
        queue = deque()
        
        # create a new matrix 
        res = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        # visit each cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res[r][c] = 0
                    queue.append((r,c))
        
        while queue:
            x,y = queue.popleft()
            
            for dx,dy in directions:
                
                # calculate next coord
                xx , yy = x + dx , y + dy
                
                # ignore if out of grid or not '-1'
                # !!!!!!!!!!!!!!!!!!!!!!!!!! because we use bfs, each water should be only set a value once, this value is surely its shortest distance to some land
                if xx < 0 or xx == rows or yy < 0 or yy == cols or res[xx][yy]!=-1:
                    continue
                    
                # update cell based on current cell
                res[xx][yy] = res[x][y] + 1
                
                # add to queue
                queue.append((xx,yy))
                
        # result is the maximum element in the matrix
        # as each cell represents the distance from the nearest 1
        result = max([max(elem) for elem in res]) 
        
        # in the case of result being 0, a path has not been found
        return result if result!=0 else -1