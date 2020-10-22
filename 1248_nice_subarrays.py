class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = []
        for i, v in enumerate(nums):
            if v % 2 != 0:
                l.append(i)
        if not l or len(l)<k:
            return 0
        r = 0
        left = 0
        right = k - 1
        while True:
            if left == 0:
                ll = 1 + l[left]
            else:
                ll = l[left] - l[left-1]
            if right == len(l) - 1:
                rr = len(nums) - l[right]
            else:
                rr = l[right+1] - l[right]
            r += ll * rr
            left += 1
            right += 1
            if right == len(l):
                return r
