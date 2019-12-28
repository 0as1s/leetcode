class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        m = 1
        count = 0
        visited = 0
        i = 0
        while True:
            if nums[i] != -1:
                count += 1
                temp = nums[i]
                nums[i] = -1
                i = temp
                visited += 1
            else:
                m = max(m, count)
                if len(nums) - visited <= m:
                    return m
                count = 0
                i += 1

s = Solution()
print(s.arrayNesting([]))
print(s.arrayNesting([0]))
print(s.arrayNesting([5,4,0,3,1,6,2]))