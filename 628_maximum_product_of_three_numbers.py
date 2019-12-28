class Solution(object):

    def maximumProduct(self, nums):
        max_ = [-float("Inf"), -float("Inf"), -float("Inf")]
        min_ = [float("Inf"), float("Inf")]
        min_max = max_[2]
        max_min = min_[1]
        for i in nums:
            if i > min_max:
                max_.append(i)
                max_ = list(reversed(sorted(max_)))[:3]
                min_max = max_[2]
            if i < max_min:
                min_.append(i)
                min_ = sorted(min_)[:2]
                max_min = min_[1]
        return max(reduce(lambda x, y: x * y, max_), max_[0] * min_[1] * min_[0])


nums = [1, 2, 3]
s = Solution()
print s.maximumProduct(nums)
