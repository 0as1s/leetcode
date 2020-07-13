class Solution(object):

    
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        r = 0
        i = 0
        while True:
            if i >= len(arr):
                return r

            if arr[i] == i:
                r += 1
                i += 1
                continue
            max_index = arr[i]
            j = i+1
            while j<=max_index:
                max_index = max(arr[j], max_index)
                j += 1
            i = j
            r += 1