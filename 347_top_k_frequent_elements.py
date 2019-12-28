class Solution(object):

    def topKFrequent(self, nums, k):
        from collections import Counter
        c = sorted(Counter(nums).iteritems(), key=lambda x: -x[1])
        return [x[0] for x in c[:k]]


nums = [1, 1, 1, 2, 2, 3]
s = Solution()
print s.topKFrequent(nums, 2)
