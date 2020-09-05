class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(mat)):
            if sum(mat[i]) != 1:
                continue
            for j in range(len(mat[0])):
                if not mat[i][j] == 1:
                    continue
                if sum([mat[x][j] for x in range(len(mat))]) == 1:
                    count += 1
        return count


s = Solution()
print(s.numSpecial([[1,0,0],
              [0,1,0],
              [0,0,1]]))
print(s.numSpecial([[1,0,0],
              [0,0,1],
              [1,0,0]]))
print(s.numSpecial([[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]))
