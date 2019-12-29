def canWin(m, used, v, table):
    if m*(m+1) / 2 < v:
        return False

    for i in range(m):
        digit = 1 << i
        if not (digit & used) and i + 1 >= v:
            return True

    if used in table.keys():
        return table[used]

    for i in range(m):
        digit = 1 << i
        if not(digit & used):
            temp = digit | used
            if not canWin(m, temp, v-i-1, table):
                table[used] = True
                return True
    table[used] = False
    return False


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger > desiredTotal:
            return True
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        used = 0
        table = {}
        return canWin(maxChoosableInteger, used, desiredTotal, table)

s = Solution()
print(s.canIWin(18, 79))