class Solution(object):
    def tra(self, digits, cur):
        if not digits:
            self.result.append(cur)
            return
        d = int(digits[0])
        for c in self.dict[d]:
            self.tra(digits[1:], cur+c)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.result = []
        self.dict = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.tra(digits, "")
        return self.result

s = Solution()
print(s.letterCombinations(""))