class Solution(object):

    def summaryRanges(self, nums):
        if not nums:
            return []
        result = []
        start = nums[0]
        end = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = nums[i + 1]
                end = nums[i + 1]
            else:
                end = nums[i + 1]
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))
        return result


nums = []
s = Solution()
print s.summaryRanges(nums)
