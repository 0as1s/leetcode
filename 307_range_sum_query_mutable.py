class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.result = []
        self.update_ = list(nums)
        s = 0
        for d in nums:
            s += d
            self.result.append(s)

    def update(self, i, val):
        self.update_[i] = val

    def sumRange(self, i, j):
        if i == j:
            return self.update_[i]
        s = self.result[j] - self.result[i] + self.nums[i]
        for index in range(i, min(j + 1, len(self.nums))):
            s += (self.update_[index] - self.nums[index])
        return s


nums = [9, -8]
s = NumArray(nums)
s.update(0, 3)
print s.sumRange(1, 1)
print s.sumRange(0, 1)
s.update(1, -3)
print s.sumRange(0, 1)
