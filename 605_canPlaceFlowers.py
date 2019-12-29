class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if n == 0:
                return True
            elif flowerbed[0] == 0:
                return True
            return False

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        for i in range(1, len(flowerbed)-1):
            if not flowerbed[i-1] and not flowerbed[i+1] and not flowerbed[i]:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1
            if not n:
                return True

        return False


s = Solution()
print(s.canPlaceFlowers([1,0,1,0,1,0,1], 1))