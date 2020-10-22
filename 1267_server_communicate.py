class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        g = [sum(x) for x in grid]
        g2 = [sum([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
        total = 0
        for i, l in enumerate(grid):
            if g[i] != 1:
                total += g[i]
                continue
            flag = False
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if g2[j] == 1:
                        flag = True
                    break
            if not flag:
                total+= 1
        return total
