class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        amount = 0
        min_ = prices[0]
        for i in range(len(prices) - 1):
            if prices[i] > prices[i+1]:
                amount += prices[i] - min_
                min_ = prices[i+1]
        if prices[-1] >= prices[-2]:
            amount += prices[-1] - min_
        return amount


s = Solution()
print(s.maxProfit([1,2,3,4,5]))
