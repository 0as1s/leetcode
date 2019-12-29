from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) in (0, 1):
            return 0
        count = 0
        m = -1
        counts = dict()
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1
            print(count)
            if count in counts.keys():
                m = max(m, i-counts[count])
            else:
                counts[count] = i
            if count == 0:
                m = i+1
            print(m)
        return m if m != -1 else len(nums)

s = Solution()
print(s.findMaxLength([0, 1, 0]))