class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        d = dict()
        visited = set()
        for a,b in zip(pattern,  str.strip().split(" ")):
            if a in d:
                if d[a] != b:
                    return False
            else:
                if b in visited:
                    return False
                d[a] = b
                visited.add(b)

        
        if len(pattern) != len(str.strip().split(" ")):
            return False
        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("", ""))
print(s.wordPattern("abba", "dog dog dog dog"))
