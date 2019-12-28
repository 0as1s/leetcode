class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dic_1 = {}
        for i in range(len(nums)):
            dic_1[i] = nums[i]
        nums = sorted(nums, key=lambda x: -x)
        dic_2 = {}
        for i in range(len(nums)):
            dic_2[nums[i]] = i
        result = []
        for i in range(len(nums)):
            r = dic_2[dic_1[i]]
            if r == 0:
                result.append("Gold Medal")
            elif r == 1:
                result.append("Silver Medal")
            elif r == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(r + 1))
        return result


s = Solution()
print s.findRelativeRanks([10, 3, 8, 9, 4])
