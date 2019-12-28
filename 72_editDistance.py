class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        matrix = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(matrix[0])):
            matrix[0][i] = i
        for i in range(len(matrix)):
            matrix[i][0] = i
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    matrix[i+1][j+1] = matrix[i][j]
                else:
                    matrix[i+1][j+1] = min(matrix[i][j] + 1, matrix[i][j+1] + 1, matrix[i+1][j] + 1)
        return matrix[-1][-1]
s = Solution()
print(s.minDistance(word1 = "intention", word2 = "execution"))