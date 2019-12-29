from collections import defaultdict


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4:
            return []
        nums = sorted(nums)
        r = set()
        sum_d = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum_d[target-nums[i]-nums[j]].append((i, j))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l = sum_d[nums[i]+nums[j]]
                for p in l:
                    if i != p[0] and i != p[1] and j != p[0] and j != p[1]:
                        r.add(tuple(sorted((nums[i], nums[j], nums[p[0]], nums[p[1]]))))
        return r
