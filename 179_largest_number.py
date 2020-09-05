class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]

        def cmp(x, y):
            if str(x+y) > str(y+x):
                return 1
            if str(x+y) == str(y+x):
                return 0
            if str(x+y) < str(y+x):
                return -1
            #return int(x+y) - int(y+x)
        #from functools import cmp_to_key
        nums = sorted(nums, cmp=cmp,reverse=True)
        if all([x=='0' for x in nums]):
            return "0"
        return "".join(nums)

s = Solution()
print(s.largestNumber([3,30,34,5,9]))
