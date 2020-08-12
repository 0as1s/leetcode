class StockSpanner(object):

    def __init__(self):
        self.back = [0]
        self.value = [float("Inf")]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if price < self.value[-1]:
            self.value.append(price)
            self.back.append(len(self.back) - 1)
            return 1
        else:
            cur = len(self.back) - 1
            while self.value[cur] <= price:
                cur = self.back[cur]
            self.value.append(price)
            self.back.append(cur)
            return len(self.value) - 1 - cur


s = StockSpanner()
print(s.next(100))
print(s.next(80))
print(s.next(60))
print(s.next(70))
print(s.next(60))
print(s.next(75))
print(s.next(85))
