from copy import deepcopy
from queue import deque

def dead_end_fill(g1, g2):
    g1 = deepcopy(g1)
    g2 = deepcopy(g2)
    dead_ends = deque()
    for i in range(len(g1) - 1):
        for j in range(len(g2) - 1):
            f = [g1[i][j], g2[i][j], g1[i+1][j], g2[i][j+1]]
            if sum(f) == 3:
                dead_ends.append((i,j))

    dead = set()
    while dead_ends:
        x, y = dead_ends.popleft()
        dead.add(cur)
        xx, yy = -1, -1
        if not g1[x][y]:
            xx, yy = x-1, y
            g1[x][y] = True
        elif not g2[x][y]:
            xx, yy = x, y-1
            g2[x][y] = True
        elif not g1[x+1][y]:
            xx, yy = x+1, y
            g1[x+1][y] = True
        elif not g2[x][y+1]:
            xx, yy = x, y+1
            g2[x][y+1] = True
        if 0 <= xx < len(g1) - 1 and 0 <= yy < len(g1[0]) - 1:
            dead_ends.append((xx, yy))
    return dead
        
