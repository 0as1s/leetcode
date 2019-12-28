from collections import defaultdict
from copy import deepcopy


def isValidSudoku(board):
    def conflict(p1, p2):
        if p1[0] == p2[0] or p1[1] == p2[1]:
            return True
        if p1[0] // 3 == p2[0] // 3 and p1[1] // 3 == p2[1] // 3:
            return True
        return False
    taken = defaultdict(set)
    for i in range(9):
        for j in range(9):
            c = board[i][j]
            if c == ".":
                continue
            for p in taken[c]:
                if conflict(p, (i, j)):
                    return False
            taken[c].add((i, j))
    return True

class Solution(object):
    def backtrack(self, left, taken_i, taken_j, taken_s, remain, board, key, po):
        s = str(board)
        if s in self.visited:
            return
        self.visited.add(s)
        board = deepcopy(board)
        left = deepcopy(left)
        taken_i = deepcopy(taken_i)
        taken_j = deepcopy(taken_j)
        taken_s = deepcopy(taken_s)
        remain = deepcopy(remain)
        print(board)
        if len(remain) == 0 and isValidSudoku(board):
            self.board = board
        if not self.board:
            available = set()
            key = 0
            for i in left.keys():
                if left[i] != 0:
                    for r in remain:
                        if r[0] not in taken_i[key] and r[1] not in taken_j[key] and (r[0] // 3, r[1] // 3) not in taken_s[key]:
                            available.add(r)
                    if not available:
                        return
            for pos in available:
                taken_i[key].add(pos[0])
                taken_j[key].add(pos[1])
                taken_s[key].add((pos[0]//3, pos[1]//3))
                left[key] -= 1
                remain.remove(pos)
                self.backtrack(left, taken_i, taken_j, taken_s, remain, board, key, pos)
                remain.add(pos)
                left[key] += 1
                taken_i[key].remove(pos[0])
                taken_j[key].remove(pos[1])
                taken_s[key].remove((pos[0] // 3, pos[1] // 3))

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.visited = set()
        remain = set()
        taken_i = defaultdict(set)
        taken_j = defaultdict(set)
        taken_s = defaultdict(set)
        left = {
            "0": 9,
            "1": 9,
            "2": 9,
            "3": 9,
            "4": 9,
            "5": 9,
            "6": 9,
            "7": 9,
            "8": 9,
            "9": 9,
        }
        self.board = None
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    remain.add((i, j))
                else:
                    taken_i[c].add(i)
                    taken_j[c].add(j)
                    taken_s[c].add((i // 3, j // 3))
                    left[c] -= 1
        key = "0"
        start = (0, 0)
        for r in remain:
            if r[0] not in taken_i[key] and r[1] not in taken_j[key] and (r[0] // 3, r[1] // 3) not in taken_s[key]:
                start = r
        remain.remove(start)
        self.backtrack(left, taken_i, taken_j, taken_s, remain, board, key, start)
        print(self.board)


s = Solution()
s.solveSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])