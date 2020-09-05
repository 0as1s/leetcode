class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = sorted(arr)
        m = arr[(len(arr) - 1) / 2]
        rr = []
        l = 0
        r = len(arr) - 1
        while len(rr) != k:
            if arr[r] - m >= m - arr[l]:
                rr.append(arr[r])
                r -= 1
            else:
                rr.append(arr[l])
                l += 1
        return rr