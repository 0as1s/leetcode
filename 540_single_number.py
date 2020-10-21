class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        while l != r:
            m = (l + r) // 2

            if m == l:
                if nums[m] != nums[m+1]:
                    if m == 0:
                        return nums[m]
                    else:
                        return nums[m]  if nums[m] != nums[m-1] else nums[m+1]
            if m == r:
                if nums[m] != nums[m-1]:
                    return nums[m]
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if nums[l] != nums[l+1]:
                if l == 0:
                    return nums[l]
                l -= 1
            if nums[r] != nums[r-1]:
                if r == len(nums)-1:
                    return nums[r]
                r += 1
            if (m - l + 1) % 2 == 1:
                if nums[m] == nums[m-1]:
                    r = m
                else:
                    l = m 
                continue
            if (m - l + 1) % 2 == 0:
                if nums[m] == nums[m-1]:
                    l = m
                else:
                    r = m 
                continue
