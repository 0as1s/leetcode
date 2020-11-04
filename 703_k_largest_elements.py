from heapq import *
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        self.k = k
        self.nums = nums
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
