class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                left = arr[i]
                right = 0
                for k in range(i+1, j+1):
                    right ^= arr[k]
                for k in range(i+1, j+1):
                    left ^= arr[k]
                    right ^= arr[k]
                    if left == right:
                        count+=1
        return count