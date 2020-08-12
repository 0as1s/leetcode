class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        left = numBottles
        while left >= numExchange:
            res += left // numExchange
            left = left // numExchange + left % numExchange
        return res

s = Solution()
print(s.numWaterBottles(15, 4))