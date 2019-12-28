from collections import defaultdict


def conflict(p1, p2):
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return True
    if p1[0] // 3 == p2[0] // 3 and p1[1] // 3 == p2[1]  // 3:
        return True
    return False

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
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

s = Solution()
print(s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
