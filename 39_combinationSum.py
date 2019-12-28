class Solution(object):
    def combinationSum(self, candidates, target):
        if target == 0 :
            return []
        dp = [set() for _ in range(target+1)]
        for c in candidates:
            if c > target:
                continue
            dp[c].add(tuple([c, ]))
        for t in range(target+1):
            for c in candidates:
                index = t-c
                if index > 0:
                    for s in dp[index]:
                        dp[t].add(tuple(sorted(s+tuple([c, ]))))
        return dp[target]

s = Solution()
print(s.combinationSum([2,3,6, 7], 7))
