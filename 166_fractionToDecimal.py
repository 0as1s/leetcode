class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = False  # <0
        if (numerator < 0 and denominator < 0) or (numerator > 0 and denominator > 0):
            sign = True
        child = abs(numerator)
        parent = abs(denominator)
        result = []
        sh = child // parent
        yu = child % parent
        if yu == 0:
            return str(sh) if sign else str(-1 * sh)
        result.append(str(sh))
        result.append(".")
        record = []
        print(sh)
        while True:
            if yu == 0:
                break
            elif yu not in record:
                record.append(yu)
                temp = yu * 10
                result.append(str(temp // parent))
                yu = temp % parent
                print(yu)
            else:
                index = record.index(yu)
                result = result[:2 + index] + ['('] + result[2 + index:] + [')']
                break

        return ''.join(result) if sign else "-" + ''.join(result)

s = Solution()
print(s.fractionToDecimal(1, 214748364))