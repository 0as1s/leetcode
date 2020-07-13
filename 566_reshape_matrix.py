class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums 
        if type(nums[0]) != list:
            return  nums
        o_r = len(nums)
        o_c = len(nums[0])
        if o_r * o_c != r*c:
            return nums
        result = [[0] * c for _ in range(r)]
        for i in range(o_r):
            for j in range(o_c):
                new_i = (i*o_c + j) // c
                new_j = (i*o_c + j) % c
                result[new_i][new_j] = nums[i][j]
        return result

