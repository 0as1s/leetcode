from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        m = float("Inf")
        result = []
        for i in range(0, len(arr)-1):
            if arr[i+1] - arr[i] == m:
                result.append([arr[i], arr[i+1]])
            elif arr[i+1] - arr[i] < m:
                result = []
                m = arr[i+1] - arr[i]
                result.append([arr[i], arr[i+1]])
        return result

arr = [0,1]
print(Solution().minimumAbsDifference([0, 1]))