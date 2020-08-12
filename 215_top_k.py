class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import *
        nums = [-x for x in nums]
        heapify(nums)
        temp = 0
        for i in range(k):
            temp = heappop(nums)
        return -temp
