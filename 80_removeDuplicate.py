class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return 2
        pre = None
        cur_count = 0
        left = 0
        total_len = 0
        for i in range(len(nums)):
            if nums[i] != pre:
                cur_count = 1
                nums[left] = nums[i]
                total_len += 1
                left += 1
                pre = nums[i]
            else:
                if cur_count != 2:
                    cur_count += 1
                    nums[left] = nums[i]
                    total_len += 1
                    left += 1
        print(total_len)
        print(nums)
        return total_len

s = Solution()
s.removeDuplicates([1,1,1,2,2,3])
s.removeDuplicates([0,0,1,1,1,1,2,3,3])
s.removeDuplicates([1,1,1,2,2,3])