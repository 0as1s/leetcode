class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        next_dict = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(-1, 0), (0, 1)]
        }
        cur = (0, 0)
        visited = set()

        possible = {
            (0, 1) : [1,3,5],
            (0, -1): [1,4,6],
            (1, 0): [2,5,6],
            (-1, 0): [2,3,4],
        }

        def valid(pos):
            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                return True
            return False
        while True:
            if cur[0] == len(grid) - 1 and cur[1] == len(grid[0]) - 1:
                return True
            visited.add(cur)
            can1_d = next_dict[grid[cur[0]][cur[1]]][0]
            can1 = (cur[0] + can1_d[0], cur[1] + can1_d[1])
            if valid(can1) and can1 not in visited and grid[can1[0]][can1[1]] in possible[can1_d]:
                cur = can1
                continue
            can1_d = next_dict[grid[cur[0]][cur[1]]][1]
            can1 = (cur[0] + can1_d[0], cur[1] + can1_d[1])
            if valid(can1) and can1 not in visited and grid[can1[0]][can1[1]] in possible[can1_d]:
                cur = can1
                continue
            if grid[0][0] != 4:
                return False
            else:
                break

        next_dict = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(1, 0), (0, 1)],
            5: [(0, -1), (-1, 0)],
            6: [(-1, 0), (0, 1)]
        }
        cur = (0, 0)
        visited = set()

        possible = {
            (0, 1) : [1,3,5],
            (0, -1): [1,4,6],
            (1, 0): [2,5,6],
            (-1, 0): [2,3,4],
        }
        while True:
            if cur[0] == len(grid) - 1 and cur[1] == len(grid[0]) - 1:
                return True
            visited.add(cur)
            can1_d = next_dict[grid[cur[0]][cur[1]]][0]
            can1 = (cur[0] + can1_d[0], cur[1] + can1_d[1])
            if valid(can1) and can1 not in visited and grid[can1[0]][can1[1]] in possible[can1_d]:
                cur = can1
                continue
            can1_d = next_dict[grid[cur[0]][cur[1]]][1]
            can1 = (cur[0] + can1_d[0], cur[1] + can1_d[1])
            if valid(can1) and can1 not in visited and grid[can1[0]][can1[1]] in possible[can1_d]:
                cur = can1
                continue
            return False

