class Solution:
    # @param n, an integer
    # @return an integer

    def __init__(self):
        self.cache = dict()

    def reverseBits(self, n):
        if n in self.cache.keys():
            return self.cache[n]
        temp = bin(n)[2:]
        temp = '0' * (32 - len(temp)) + temp
        result = int(temp[::-1], base=2)
        self.cache[n] = result
        return result


s = Solution()
print s.reverseBits(43261596)
