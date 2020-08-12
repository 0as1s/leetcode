class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=lambda x: -len(x))
        store = dict()
        for w in words:
            l = len(w)
            s = set(w)
            key = "".join(sorted(s))
            if key not in store:
                store[key] = (l, s)
        keys = sorted(list(store.keys()), key=lambda x: -store[x][0])
        m = 0
        for i in range(len(keys)):
            k1 = keys[i]
            if store[k1][0] * store[k1][0] < m:
                return m
            for j in range(i+1, len(keys)):
                k2 = keys[j]
                if not store[k1][1] & store[k2][1]:
                    m = max(m, store[k1][0] * store[k2][0])
                    break
        return m

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(s.maxProduct(["a","aa","aaa","aaaa"]))
print(s.maxProduct(["edadc","ebbfe","aacdde","dfe","cb","fddddff","fabca","adccac","ece","ccaf","feba","bcb","edadc","aea","bacb","acefa","fcebffd","dfeebca","bedcbaa","deaccc","abedc","dadff","eef","ddebbb","abecab","cd","abdeee","eedce","deef","dceaddd","ced","fbbf","ba","eefeda","fb","cddc","adafbf","dded","aadbf","caefbaf","ccebf","dbb","ee","dadcecc","ddbcabb","afeaa","ec","aad","efde","cbcda","cdbdafd","cddc","ecaaa","ae","cfc","bccac","cdcc","abbbf","fcdface","ddbcdc","bfebb","daed","bc","dc","ecdfc","eeb","bb","dad","caecb","fbe","bbbc","cacea","dbc","fbe","bcfffbd","aeda","cff","ddfc","ea","bdfd","ccb","cb","ae","ceabefa","dcea","cbaed","bfedf","fa","ccd","fece","bceef","acabca","dafa","fdeec","dac","cae","adeeadb","ecacc","acfe","de"]))
