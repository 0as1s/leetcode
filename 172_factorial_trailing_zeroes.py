class Solution(object):

    def trailingZeroes(self, n):
        if n < 5:
            return 0
        i = 1
        result = 0
        import math
        while(True):
            temp = n / int(math.pow(5, i))
            if temp == 0:
                return result
            else:
                result += temp
                i += 1
s = Solution()
print s.trailingZeroes(30)
