class Solution(object):
    def lexicalOrder(self, n):
        
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 10:
            return list(range(1, n+1))
        stack = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        res = []
        while stack:
            r = stack.pop()
            res.append(r)
            for i in range(9, -1, -1):
                if r * 10 + i <= n:
                    stack.append(r * 10 + i)
        return res

s = Solution()
print(s.lexicalOrder(192))
