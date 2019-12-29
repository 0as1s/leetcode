from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = "".join([x for x in licensePlate if x not in " 1234567890" ])
        c = Counter(licensePlate.lower())
        total = sum(c.values())
        words = sorted(words, key=lambda x: len(x))
        for w in words:
            if len(w) < total:
                continue
            c2 = Counter(w.lower())
            flag = 0
            for k in c.keys():
                if c2.get(k, 0) < c[k]:
                    flag = 1
                    break
            if flag == 0:
                return w


s = Solution()
print(s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]))