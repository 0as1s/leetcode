class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        left = 0
        right = k
        if k == 0:
            return False
        from collections import defaultdict
        count = defaultdict(int)
        for i in range(left, right+1):
            count[nums[i]] += 1
            if count[nums[i]] == 2:
                return True
        for i in range(len(nums) - right - 1):
            count[nums[left]] -= 1
            left += 1
            right += 1
            count[nums[right]] += 1
            if count[nums[right]] == 2:
                return True
        return False

s = Solution()
print(s.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(s.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
