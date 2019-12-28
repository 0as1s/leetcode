class Solution(object):

    def multiply_by_one(self, num, d):
        result = [0] * (len(num) + 1)
        C = 0
        for i in range(len(num) - 1, -1, -1):
            temp = d * num[i] + C
            C = temp / 10
            result[i + 1] = temp % 10
        result[0] = C
        return result if C else result[1:]

    def add(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        # print num1
        # print num2
        if l1 < l2:
            num2, num1 = num1, num2
        num1 = [0] + num1
        l1 = len(num1)
        C = 0
        for i in range(l2):
            temp = num1[l1 - 1 - i] + num2[l2 - 1 - i] + C
            C = temp / 10
            num1[l1 - 1 - i] = temp % 10
            # print C, num1[l1 - 1 - i]
        if C == 0:
            return num1[1:]
        for i in range(l1 - l2 - 1, -1, -1):
            temp = num1[i] + C
            num1[i] = temp % 10
            C = temp / 10
            if C == 0:
                return num1 if num1[0] else num1[1:]
        return [1] + num1[1:]

    def multiply(self, num1, num2):
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = map(lambda x: int(x), num1)
        num2 = map(lambda x: int(x), num2)
        l = len(num1)
        result = self.multiply_by_one(num2, num1[-1])
        for i in range(1, l):
            temp = self.multiply_by_one(num2, num1[l - 1 - i]) + [0] * i
            # print temp
            result = self.add(temp, result)
            # print result
            # print '============'
        result = "".join(map(lambda x: str(x), result))
        count = 0
        for i in range(len(result)):
            if result[i] == '0':
                count += 1
            else:
                break
        result = result[count:]
        return result or "0"
        # return "".join(map(lambda x: str(x), result))


s = Solution()
# print s.multiply("12345", "978")
# print s.multiply("12345", "6780")
# print s.multiply("12345", "67891")
# print s.multiply("12345", "67890")
print s.multiply("9333", "0")
s.add([9, 1, 2, 0], [1, 3, 6, 8])
# print s.add([1, 3, 6, 8], [9, 1, 2, 0])
