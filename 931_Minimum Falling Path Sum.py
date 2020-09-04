class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(A)):
            for j in range(len(A)):
                candidates = []
                for k in (-1, 0, 1):
                    if 0 <= j+k < len(A):
                        candidates.append(A[i][j] + A[i-1][j+k])
                A[i][j] = min(candidates)
        return min(A[-1])

s = Solution()
s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])