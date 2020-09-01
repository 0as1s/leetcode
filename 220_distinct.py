class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= t:
            for i in range(len(nums)):
                for j in range(1, k+1):
                    if i+j >= len(nums):
                        break
                    if abs(nums[i+j] - nums[i]) <= t:
                        return True
        else:
            last = dict()
            for i in range(len(nums)):
                for j in range(-t, t+1):
                    if nums[i]+j in last and abs(last[nums[i]+j] - i) <= k:
                        return True
                last[nums[i]] = i
        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate([7,1,3], 2, 3))
