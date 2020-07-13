class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        

        min_dict = [50001]  * 50000
        max_dict = [0] * 50000

        for i, v in enumerate(A):
            min_dict[v] = min(min_dict[v], i)
            max_dict[v] = max(max_dict[v], i)

        for i in range(1, len(min_dict)):
            min_dict[i] = min(min_dict[i], min_dict[i-1])
        
        for i in range(len(max_dict)-2, -1, -1):
            max_dict[i] = max(max_dict[i+1], max_dict[i])
        
        max_ramp = 0
        for i, j in zip(min_dict, max_dict):
            max_ramp = max(max_ramp, j-i)

