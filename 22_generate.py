class Solution(object):
    def recursive(self, n, depth, cur):
        # print(cur)
        if depth < 0:
            return
        if n == 0:
            # print(depth)
            if depth == 0:
                # print("0")
                self.result.append(cur)
            return
        self.recursive(n-1, depth+1, cur+"(")
        self.recursive(n-1, depth-1, cur+")")

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.recursive(n*2, 0, "")
        return self.result
