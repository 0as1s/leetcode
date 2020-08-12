class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        while c:
            size = 0
            idx = min(c.keys())
            while size < k:
                if idx not in c:
                    return False
                c[idx] -= 1
                size += 1
                if c[idx] == 0:
                    del c[idx]
                idx += 1
        return True