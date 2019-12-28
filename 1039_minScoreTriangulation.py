class Solution:
    def minScoreTriangulation(self, A):
        n = len(A)
        dp = [[float('inf')] * n for _ in range(n)]
        for j in range(n):
            for i in range(j-1,-1,-1):
                if j - i < 2:
                    dp[i][j] = 0
                else:
                    for k in range(i+1,j):
                        dp[i][j] = min(dp[i][j],A[i]*A[j]*A[k]+dp[i][k]+dp[k][j])
        return dp[0][n-1]

s = Solution()
# print(s.minScoreTriangulation([1,3,1,4,1,5]))
# print(s.minScoreTriangulation([3,7,4,5]))
print(s.minScoreTriangulation([2,1,4,4]))
