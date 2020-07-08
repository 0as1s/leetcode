class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        max_sum = 0
        cur_sum = 0
        for i in arr:
            cur_sum = max(cur_sum+i, i)
            max_sum = max(max_sum, cur_sum)
        if k == 1:
            return max_sum % (10 ** 9 + 7)

        arr_sum = sum(arr)

        continuous_max_sum = 0
        continuous_cur_sum = 0
        continuous_max_sum_reversed = 0
        continuous_cur_sum_reversed = 0

        for i in arr:
            continuous_cur_sum = continuous_cur_sum + i
            continuous_max_sum = max(continuous_max_sum, continuous_cur_sum)
        for i in reversed(arr):
            continuous_cur_sum_reversed = continuous_cur_sum_reversed + i
            continuous_max_sum_reversed = max(continuous_max_sum_reversed, continuous_cur_sum_reversed)

        repeat_sum = (k-2)*arr_sum
        result = max(repeat_sum + continuous_max_sum + continuous_max_sum_reversed, max_sum)

        return result % (10 ** 9 + 7)


s=Solution()
print(s.kConcatenationMaxSum([1,0,4,1,4], 4))
