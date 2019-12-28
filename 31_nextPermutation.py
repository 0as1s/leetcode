from bisect import bisect_left

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                flag = False
        l = len(nums)
        if flag:
            for i in range(l//2):
                nums[i], nums[l-i-1] = nums[l-i-1], nums[i]
            return
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                temp = i
                for i in range(len(nums) -1, i, -1):
                    if nums[i] > nums[temp]:
                        t = nums[i]
                        del nums[i]
                        nums.insert(temp, t)
                        to_exchange = len(nums) - 1
                        for i in range(len(nums) - 2, temp, -1):
                            if nums[i] >= nums[i+1]:
                                to_exchange = i
                            else:
                                break
                        # print(to_exchange)
                        for i in range(0, (l-to_exchange) // 2):
                            nums[to_exchange + i], nums[l-i-1] = nums[l-i-1], nums[to_exchange + i]
                        to_insert = bisect_left(nums[temp+2:], nums[temp+1])
                        nums.insert(to_insert + temp + 2, nums[temp+1])
                        del nums[temp+1]
                        # print(nums)
                        return

s = Solution()
s.nextPermutation([1,3,2])
s.nextPermutation([2,3,1])
s.nextPermutation([5,4,7,5,3,2])