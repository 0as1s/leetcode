class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i_m, m = 0, -float("Inf")
        for i, v in enumerate(arr):
            if v > m:
                i_m = i
                m = v
        if k >= i_m:
            return m
        length = 0
        cur_max = arr[0]
        cur = 1
        flag = True
        while cur != i_m:
            if cur_max > arr[cur]:
                cur += 1
                length += 1
                if length == k:
                    return cur_max
            else:
                if k == 1:
                    return arr[cur]
                cur_max = arr[cur]
                cur += 1
                length = 1
        return m

s = Solution()
print(s.getWinner([2,1,3,5,4,6,7],2))
print(s.getWinner([1,9,8,2,3,7,6,4,5], 7))
