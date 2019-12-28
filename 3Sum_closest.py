class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest = 99999
        if len(nums) == 3:
            return sum(nums)
        for i in range(1, len(nums) - 1):
            j = 0
            k = len(nums) - 1
            while(True):
                if abs(nums[i] + nums[k] + nums[j] - target) < abs(closest - target):
                    closest = nums[i] + nums[k] + nums[j]
                if nums[i] + nums[k] + nums[j] < target:
                    if j == i - 1:
                        break
                    j += 1

                if abs(nums[i] + nums[k] + nums[j] - target) < abs(closest - target):
                    closest = nums[i] + nums[k] + nums[j]
                if nums[i] + nums[k] + nums[j] > target:
                    if k == i + 1:
                        break
                    k -= 1
                if nums[i] + nums[k] + nums[j] == target:
                    return target
                if abs(nums[i] + nums[k] + nums[j] - target) < abs(closest - target):
                    closest = nums[i] + nums[k] + nums[j]
        return closest


s = Solution()
print s.threeSumClosest([0, 2, 1, -3], 1)
