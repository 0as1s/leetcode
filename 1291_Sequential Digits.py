class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        for s in range(1, 10):
            ss = s
            cur = s
            r = []
            while True:
                cur += 1
                if cur == 10:
                    break
                if low <= ss <= high:
                    r.append(ss)
                ss = ss * 10 + cur
                if ss > high:
                    break
        return sorted(r)