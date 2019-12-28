class Solution(object):
    def recursive(self, board, word, used, i, j):
        # print(used)
        if self.result:
            return
        if len(word) == 1:
            self.result = True
            return
        # if used[i][j]:
        #     return
        for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            i_, j_ = i+d[0], j+d[1]
            if 0<=i_<len(board) and 0<=j_<len(board[0]) and not used[i_][j_] and board[i_][j_] == word[1]:
                used[i][j] = True
                self.recursive(board, word[1:], used, i_, j_)
                used[i][j] = False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board or not board[0]:
            return False
        self.result = False
        proposals = []
        used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    proposals.append((i, j))
        for i, j in proposals:
            self.recursive(board, word, used, i, j)
        return self.result

s = Solution()
print(s.exist(board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],  word = "ABCCED"))
print(s.exist(board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],  word = "SEE"))
print(s.exist(board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],  word = "ABCB"))