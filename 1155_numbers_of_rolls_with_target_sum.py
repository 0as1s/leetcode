class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        from collections import defaultdict
        store = defaultdict(int)
        for i in range(1, f+1):
            store[(1, i)] = 1
        for j in range(2, 2*f+1):
            store[(2, j)] = min(f, j-1) - max(j-f, 1) + 1
        for d in range(3, d+1):
            for t in range(d, d*f+1):
                for ff in range(1, f+1):
                    store[(d, t)] += store[(d-1, t-ff)]
        return store[(d, target)] % (10 ** 9 + 7)

s = Solution()
#print(s.numRollsToTarget(d = 1, f = 6, target = 3))
#print(s.numRollsToTarget(d = 2, f = 6, target = 7))
#print(s.numRollsToTarget(d = 2, f = 5, target = 10))
#print(s.numRollsToTarget(d = 1, f = 2, target = 3))
print(s.numRollsToTarget(d = 30, f = 30, target = 500))
