from collections import Counter

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        count_A = Counter(A)
        count_B = Counter(B)
        if len(count_A.keys()) == 1 or len(count_B.keys()) == 1:
            return 0
        can = None
        total = 0
        for k in count_A.keys():
            if count_A[k] + count_B.get(k, 0) >= len(A):
                can = k
                total = count_A[k] + count_B[k]
        if not can:
            return -1
        for a, b in zip(A, B):
            if a != can and b != can:
                return -1
            if a == b:
                total -= 1
                if total <  len(A):
                    return -1
        return min(len(A) - count_A[can], len(B) - count_B[can])

s = Solution()
print(s.minDominoRotations(A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]))
print(s.minDominoRotations(A = [3,5,1,2,3], B = [3,6,3,3,4]))
print(s.minDominoRotations([1,2,3,4,6], [6,6,6,6,5]))