class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter, defaultdict
        t = max(nums)
        c = Counter(nums)
        m = 0
        cur_sum = 0
        pick = defaultdict(int)
        not_pick = defaultdict(int)
        for i in range(1, t+1):
            pick[i] = not_pick[i-1] + c.get(i, 0) * i
            not_pick[i] = max(not_pick[i-1], pick[i-1])
        return max(pick[t], not_pick[t])
    
