class Solution(object):
    def tra(self, picked, remain):
        self.result.add(tuple(picked))
        if not remain:
            return
        self.tra(picked, remain[1:])
        picked.append(remain[0])
        self.tra(picked, remain[1:])
        del(picked[-1])

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.result = set()
        self.tra([], nums)
        return self.result

s = Solution()
