from typing import List


class Solution:
    def recursive(self, left, turn, score_1, score_2, total_left):
        if turn == 0: # 甲
            if score_1 >= score_2 + total_left:
                return True
            if not left:
                return False
        if turn == 1: # 乙
            if score_2 > score_1 + total_left:
                return True
            if not left:
                return False
        if turn == 0:
            case1 = self.recursive(left[1:], 1, score_1 + left[0], score_2, total_left - left[0])
            if not case1:
                return True
            case2 = self.recursive(left[:-1], 1, score_1 + left[-1], score_2, total_left - left[-1])
            if not case2:
                return True
            return False
        if turn == 1:
            case1 = self.recursive(left[1:], 0, score_1, score_2 + left[0], total_left - left[0])
            if not case1:
                return True
            case2 = self.recursive(left[:-1], 0, score_1, score_2 + left[-1], total_left - left[-1])
            if not case2:
                return True
            return False

    def PredictTheWinner(self, nums: List[int]) -> bool:
        total_left = sum(nums)
        return self.recursive(nums, 0, 0, 0, total_left)


s = Solution()
arr = [306416,2889306,7742619,3897090,6904996,1954213,8815586,9031637,256723,4662300,3024674,5433146,8190137,5093129,9258336,3161122,3217503,1331124,9213976,8810715]
print(s.PredictTheWinner(arr))