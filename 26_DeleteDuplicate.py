class Solution(object):
    def removeDuplicates(self, nums):
        count = 0
        pre = float("Inf")
        for n in nums:
            if n!= pre:
                nums[count] = n
                pre = n
                count += 1
        return count