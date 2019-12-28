class Solution(object):
    def min_coin(self, coins, amount):
        s = []
        if amount in self.cache:
            return self.cache[amount]
        if amount in coins:
            return 1
        if amount < 0:
            return float("Inf")
        for c in coins:
            s.append(self.min_coin(coins, amount - c) + 1)
        self.cache[amount] = min(s)
        return self.cache[amount]

    def coinChange(self, coins, amount):
        if 0 in coins:
            coins.remove(0)
        if amount == 0:
            return 0
        if not coins:
            return -1
        self.cache = dict()
        m = self.min_coin(coins, amount)
        if m == float("Inf"):
            return -1
        return m

s = Solution()
print(s.coinChange([243,291,335,209,177,345,114,91,313,331],7367))