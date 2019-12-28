class Solution(object):
    def one_pass(self, nums):
        total = list(nums)
        set1 = set()
        set2 = set()
        for i in range(len(nums)):
            if i == 0:
                total[i] = nums[0]
                set1.add(i)
                continue
            if i == 1:
                if nums[i] > nums[0]:
                    set2.add(i)
                    total[i] = nums[i]
                else:
                    set2.add(0)
                    total[i] = nums[0]
                continue
            if total[i-1] >= total[i-2] + nums[i]:
                total[i] = total[i-1]
                set1, set2 = set2, set1
            else:
                total[i] = total[i-2] + nums[i]
                set1.add(i)
                set1, set2 = set2, set1
        if len(nums) - 1 in set2 and 0 in set2:
            return total[len(nums)-2], True
        else:
            return total[len(nums)-1], False

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        total_1, conflict = self.one_pass(nums)
        if not conflict:
            return total_1
        total_2, _ = self.one_pass(list(reversed(nums)))
        return max(total_1, total_2)


s = Solution()
print(s.rob([8,9,9,4,10,5,6,9,7,9]))
