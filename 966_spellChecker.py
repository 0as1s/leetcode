def replace_aeiou(w):
    for c in 'aeiou':
        w = w.replace(c, "~")
    return w


class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        direct = set(wordlist)
        to_lower = dict()
        replace = dict()
        for w in wordlist:
            lower = w.lower()
            if lower not in to_lower.keys():
                to_lower[lower] = w
            for c in 'aeiou':
                lower = lower.replace(c, "~")
            if lower not in replace.keys():
                replace[lower] = w

        r = [""] * len(queries)
        for i, q in enumerate(queries):
            if q in direct:
                r[i] = q

        queries = [(x.lower(), i) for i, x in enumerate(queries) if not r[i]]
        for lower, i in queries:
            r[i] = to_lower.get(lower, "")

        queries = [(replace_aeiou(x), i) for x, i in queries if not r[i]]
        for r_, i in queries:
            r[i] = replace.get(r_, "")
        return r


s = Solution()
print(s.spellchecker(wordlist = ["KiTe","kite","hare","Hare", "iaf"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto", "AIF"]))
