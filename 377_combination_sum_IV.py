class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from copy import deepcopy
        from collections import defaultdict
        result = defaultdict(list)
        for n in nums:
            result[n] = [defaultdict(int), ]
            result[n][0][n] = 1
        for i in range(min(nums), target+1):
            for n in nums:
                if i-n in result:
                    cp = deepcopy(result[i-n])
                    for item in cp:
                        item[n] += 1
                    result[i].extend(cp)
            print(result[i])
        # print(result[i])
        
        
s = Solution()
s.combinationSum4([4,2,1], 32)