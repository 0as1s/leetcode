class Solution(object):

    def candy(self, ratings):
        if not ratings:
            return 0
        l = len(ratings)
        if l == 1:
            return 1
        i = 0
        result = [0] * l
        result[0] = 1
        while(True):
            if ratings[i + 1] > ratings[i]:
                result[i + 1] = result[i] + 1
            if ratings[i + 1] == ratings[i]:
                result[i + 1] = 1
            if ratings[i + 1] < ratings[i]:
                if i - 1 >= 0 and ratings[i - 1] < ratings[i]:
                    result[i + 1] = 1
                else:
                    result[i + 1] = result[i] - 1
                if result[i + 1] <= 0 and (i + 2 == l or ratings[i + 2] >= ratings[i + 1]):
                    result[i + 1] = 1
                    for j in range(i + 1):
                        i_j = ratings[i - j]
                        i_j_1 = ratings[i - j + 1]
                        if i_j < i_j_1:
                            break
                        if (i - j - 1 >= 0 and i_j > ratings[i - j - 1] and i_j > i_j_1):
                            result[i - j] = max(
                                result[i - j + 1] + 1, result[i - j - 1] + 1)

                        elif i_j > i_j_1:
                            result[i - j] = result[i - j + 1] + 1
                        elif i_j == i_j_1:
                            if i - j - 1 >= 0 and ratings[i - j - 1] >= i_j:
                                result[i - j] = 1
                            elif i - j == 0:
                                result[i - j] = 1
                        else:
                            break
            i += 1
            if i == l - 1:
                break
        return sum(result)


num = [1, 2, 3, 4, 5]
num = [5, 4, 3, 2, 1]
num = [1, 2, 3, 2, 1]
num = [1, 2, 2, 3, 4, 3, 2, 3, 4, 5, 2, 1]
# num = [1, 2, 2]
# num = [2, 2, 1]
# num = [1, 3, 4, 3, 2, 1]
# num = [5, 1, 1, 1, 10, 2, 1, 1, 1, 3]
# num = [2, 1, 1]
# num = [
#     58, 21, 72, 77, 48, 9, 38, 71, 68, 77, 82, 47, 25, 94, 89, 54, 26, 54, 54, 99, 64, 71, 76, 63, 81, 82, 60, 64, 29, 51, 87, 87, 72, 12, 16, 20, 21, 54, 43, 41, 83, 77, 41, 61, 72, 82, 15, 50, 36,
#       69, 49, 53, 92, 77, 16, 73, 12, 28, 37, 41, 79, 25, 80, 3, 37, 48, 23, 10, 55, 19, 51, 38, 96, 92, 99, 68, 75, 14, 18, 63, 35, 19, 68, 28, 49, 36, 53, 61, 64, 91, 2, 43, 68, 34, 46, 57, 82, 22, 67, 89]
# num = [1, 2, 2, 1]
s = Solution()
print s.candy(num)
