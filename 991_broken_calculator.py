class Solution(object):
    def gt(self, cur, Y):
        count = 0
        while cur < Y:
            cur *= 2
            count += 1
        count += (cur - Y)
        return count
    def helper(self, cur, Y):
        if Y < cur:
            return cur-Y
        if cur == Y:
            return 1
        if Y % 2 == 1:
            return min(self.gt(cur, Y), self.helper(cur, (Y+1)//2) + 2)
        else:
            return min(self.gt(cur, Y), self.helper(cur, Y//2) + 1)


    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X==Y:
            return 0
        self.visited = set()
        self.m = 0
        t = X
        while t<Y:
            t*=2
            self.m+=1
        return self.helper(X, Y)
        
s = Solution()
print(s.brokenCalc(3,100))
