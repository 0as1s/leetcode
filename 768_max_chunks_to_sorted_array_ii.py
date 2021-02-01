class Solution(object):
    def find_one_chunk(self, arr, sorted_arr):
        if not arr:
            return 0
        cur_min = arr[0]
        cur_max = arr[0]

        for i in range(len(arr)):
            cur_min = min(cur_min, arr[i])
            cur_max = max(cur_max, arr[i])
            if cur_min == sorted_arr[0] and cur_max == sorted_arr[i]:
                return 1 + self.find_one_chunk(arr[i+1:], sorted_arr[i+1:])
        
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict
        counted = defaultdict(int)
        new_arr = []
        for a in arr:
            new_arr.append((a, counted[a]))
            counted[a] += 1
        sorted_new = sorted(new_arr)
        return self.find_one_chunk(new_arr, sorted_new)
