class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        even = []
        odd = []
        if arr[0] % 2 == 1:
            odd.append(1)
            even.append(0)
        else:
            odd.append(0)
            even.append(1)

        for a in arr[1:]:
            if a % 2 == 1:
                t = odd[-1]
                odd.append(even[-1]+1)
                even.append(t)
            else:
                even.append(even[-1]+1)
                odd.append(odd[-1])
        return sum(odd)
