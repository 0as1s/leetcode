from collections import defaultdict
from random import random

class Solution(object):
    def __init__(self, nums):
        self.d = defaultdict(list)
        while nums:
            self.d[nums.pop()].append(len(nums))

    def pick(self, target):
        l =  self.d[target]
        if len(l) == 1:
            return l[0]
        factor = 1 / len(l)
        r = random()
        if r == 1:
            r = random()

        for i in range(len(l)):
            if factor*i <= r < factor * (i+1):
                return l[i]


s = Solution([1,2, 2,3,3,3])
print(s.pick(2))
