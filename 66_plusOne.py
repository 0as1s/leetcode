class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits
        result = [0] * (len(digits) + 1)
        c = 0
        r = 0
        for i in range(len(digits), 0, -1):
            j = i - 1
            r = digits[j] + c
            if j == len(digits) - 1:
                r += 1
            c = r // 10
            r = r % 10
            result[i] = r
        if c == 1:
            result[0] = 1
        return result[1:] if result[0] == 0 else result

s = Solution()
print(s.plusOne([0]))
