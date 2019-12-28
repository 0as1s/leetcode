class Solution(object):

    def removeKdigits(self, num, k):
        l = len(num)
        if l == k:
            return "0"
        if l == k + 1:
            return str(min(num))
        num = map(lambda x: int(x), num)
        pre = 0
        result = []
        for i in range(k, l):
            m = min(num[pre:i + 1])
            pre = num.index(m, pre, i + 1) + 1
            result.append(m)
        count = 0
        for i in range(len(result)):
            if result[i] == 0:
                count += 1
            else:
                break
        if count == len(result):
            return "0"
        return "".join(map(lambda x: str(x), result[count:]))


s = Solution()
print s.removeKdigits("1432219", 3)
