from collections import Counter, defaultdict


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        c = Counter(nums)
        m = max(c.values())
        # print(m)
        max_l = float("Inf")
        l, r = 0, 1
        table = defaultdict(int)
        table[nums[l]] = 1
        while True:
            table[nums[r]] += 1
            print(table)
            while table[nums[r]] >= m:
                max_l = min(max_l, r-l+1)
                # print(l, r)
                table[nums[l]] -= 1
                l += 1
            r += 1
            if r == len(nums):
                break
        return max_l


s = Solution()
print(s.findShortestSubArray([1,2,2,3,1,4,2]))