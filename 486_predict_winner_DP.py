from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        l = nums
        dp = [[0, ] * len(l) for _ in range(len(l))]

        for i in range(len(l)):
            if len(l) % 2 == 0:
                dp[i][i] = -l[i]
            else:
                dp[i][i] = l[i]
        for s in range(1, len(l)):
            for i in range(len(l)-s):
                j = i+s
                dp[i][j] = max(dp[i][i] - dp[i+1][j], dp[j][j] - dp[i][j-1])
        # print(dp)
        # print(dp)

        return True if dp[0][len(l)-1] >= 0 else False


s = Solution()
print(s.PredictTheWinner([1, 5, 2]))