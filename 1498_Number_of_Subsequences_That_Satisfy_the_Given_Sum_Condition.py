class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        res = 0
        # cur = pow(1, len(nums))
        cur = 1
        cur = cur << len(nums)
        while left <= right:
            cur = cur >> 1
            if nums[left] + nums[right] > target:
                res += cur
                right -= 1
            else:
                left += 1
        left = 1
        left = left << len(nums)
        left -= (1 + res)
        return left % (10 ** 9 + 7)
        # return int((pow(2, len(nums)) - res) % (10 ** 9 + 7)) - 1

s = Solution()
print(s.numSubseq([3,5,6,7], 9))
print(s.numSubseq([3,3,6,8], 10))
print(s.numSubseq([2,3,3,4,6,7], 12))
print(s.numSubseq([5,2,4,1,7,6,8], 16))
