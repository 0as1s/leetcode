from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for n in nums:
            if n!= val:
                nums[count] = n
                count += 1
        return count
