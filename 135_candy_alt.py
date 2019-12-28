class Solution(object):

    def candy(self, ratings):
        if not ratings:
            return 0
        l = len(ratings)
        if l == 1:
            return 1

        result1 = [0] * l
        result1[0] = 1
        result1[-1] = 1
        result2 = [0] * l
        result2[0] = 1
        result2[-1] = 1

        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                result1[i] = result1[i - 1] + 1
            else:
                result1[i] = 1

        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result2[i] = result2[i + 1] + 1
            else:
                result2[i] = 1
        return sum([max(result1[i], result2[i]) for i in range(l)])
num = [
    58, 21, 72, 77, 48, 9, 38, 71, 68, 77, 82, 47, 25, 94, 89, 54, 26, 54, 54, 99, 64, 71, 76, 63, 81, 82, 60, 64, 29, 51, 87, 87, 72, 12, 16, 20, 21, 54, 43, 41, 83, 77, 41, 61, 72, 82, 15, 50, 36,
      69, 49, 53, 92, 77, 16, 73, 12, 28, 37, 41, 79, 25, 80, 3, 37, 48, 23, 10, 55, 19, 51, 38, 96, 92, 99, 68, 75, 14, 18, 63, 35, 19, 68, 28, 49, 36, 53, 61, 64, 91, 2, 43, 68, 34, 46, 57, 82, 22, 67, 89]
# num = [1, 2, 2, 1]
s = Solution()
print s.candy(num)
