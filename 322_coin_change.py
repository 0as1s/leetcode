class Solution(object):

    def __init__(self):
        self.result = []

    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if not coins:
            return -1
        coins = sorted(coins, key=lambda x: -x)
        self.f(coins, amount, 0)
        if not self.result:
            return -1
        return min(self.result)

    def f(self, coins, amount, num):
        if not coins:
            return
        new_num = num + 1
        if coins[0] == amount:
            self.result.append(new_num)
            return
        else:
            new_amount = amount - coins[0]
            if new_amount > 0:
                self.f(coins, new_amount, new_num)
                self.f(coins[1:], new_amount, new_num)
            else:
                self.f(coins[1:], amount, num)


s = Solution()
print s.coinChange([1, 2, 5], 18)
