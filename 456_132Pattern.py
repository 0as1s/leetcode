class Solution(object):

    def find132pattern(self, nums, max_=None, index=None):
        if len(nums) < 3:
            return False
        a = set()
        for i in nums:
            a.add(i)
        if len(a) <= 2:
            return False
        if len(nums) > 900:
            if nums[0] < nums[1]:
                temp1 = nums[::2]
                temp2 = nums[1::2]
                flag_1 = 0
                flag_2 = 0
                for i in range(len(temp1) - 1):
                    if temp1[i] < temp1[i + 1]:
                        break
                else:
                    flag_1 = 1
                for i in range(len(temp2) - 1):
                    if temp2[i] > temp2[i + 1]:
                        break
                else:
                    flag_2 = 1
                if flag_1 and flag_2:
                    return False
            if nums[1] < nums[0]:
                temp1 = nums[::2]
                temp2 = nums[1::2]
                flag_1 = 0
                flag_2 = 0
                for i in range(len(temp1) - 1):
                    if temp1[i] > temp1[i + 1]:
                        break
                else:
                    flag_1 = 1
                for i in range(len(temp2) - 1):
                    if temp2[i] < temp2[i + 1]:
                        break
                else:
                    flag_2 = 1
                if flag_1 and flag_2:
                    return False

        if not max_ or not index:
            max_ = nums[0]
            index = 0
            for i, m in enumerate(nums):
                if m > max_:
                    max_ = m
                    index = i
        if index == 0:
            return self.find132pattern(nums[index + 1:])
        min_ = min(nums[:index])
        for n in nums[index + 1:]:
            if not n == max_:
                break
        else:
            return self.find132pattern(nums[:index])
        middle = -999999999
        n_index = 0
        for i, n in enumerate(nums[index + 1:]):
            if n > middle and n != max_:
                middle = n
                n_index = i
        if min_ < middle < max_:
            return True
        else:
            return self.find132pattern(nums[:index]) or self.find132pattern(nums[index + 1:], max_=middle, index=n_index)


s = Solution()
# print s.find132pattern([-1, 3, 2, 0])
# print s.find132pattern([3, 1, 4, 2])
# print s.find132pattern([50, 70, 20, 40, 10, 51])
# print s.find132pattern([90, 100, 50, 70, 20, 40, 10, 51])
# print s.find132pattern([2, 3, 4, 1])
# print s.find132pattern([1, 3, 2, 4])
print s.find132pattern([26, 26, 16, 16, 36, 36, 26, 26, 56, 56])
