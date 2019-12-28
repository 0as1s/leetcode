import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        l = 0
        r = len(matrix)
        mid = 0
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False
        while l < r:
            mid = (l + r )// 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            if matrix[mid][0] > target:
                r = mid
            else:
                l = mid + 1
        index = bisect.bisect_left(matrix[mid], target)
        if index == len(matrix[mid]):
            return False
        if matrix[mid][index] == target:
            return True
        return False

s = Solution()
print(s.searchMatrix(matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], target=13))

print(s.searchMatrix(matrix=[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], target=8))