class Solution(object):
    def tra(self, left, cur):
        if not left:
            self.result.add(tuple(cur))
        for l in left:
            temp1 = list(left)
            temp1.remove(l)
            # temp2 = list(cur)
            # temp2.append(l)
            cur.append(l)
            self.tra(temp1, cur)
            del[cur[-1]]



    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.result = set()
        self.tra(nums, [])
        return self.result
        # print(self.result)


s= Solution()
s.permuteUnique([1,1,2])
s.permuteUnique([])
