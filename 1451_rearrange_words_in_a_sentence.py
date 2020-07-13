class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        from collections import defaultdict
        length_words = defaultdict(list)
        words = text.split(" ")
        words[0] = words[0].lower()
        for word in words:
            length_words[len(word)].append(word)
        res = []
        for k in sorted(list(length_words.keys())):
            res.extend(length_words[k])
        start = res[0]
        start = start[0].upper() + start[1:]
        res[0] = start
        return " ".join(res)
