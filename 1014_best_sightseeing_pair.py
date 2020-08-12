class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr1 = [A[x]+x for x in range(len(A))]
        arr2 = [x-A[x] for x in range(len(A))]
        max_from_left = [arr1[0],]
        for a in arr1[1:]:
            max_from_left.append(max(a, max_from_left[-1]))
        min_from_right = [arr2[-1]]

        for i in range(len(arr2)-2, -1, -1):
            a = arr2[i]
            min_from_right.append(min(a, min_from_right[-1]))

        min_from_right = list(reversed(min_from_right))
        max_delta = 0
        
        for i in range(len(max_from_left)-1):
            max_delta = max(max_delta, (max_from_left[i] - min_from_right[i+1]))
        return max_delta
        
s = Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6]))