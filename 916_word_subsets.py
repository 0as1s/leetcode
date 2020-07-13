class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict, Counter
        
        max_len_in_A = 0
        letter_count = defaultdict(int)
        for b in B:
            letter_in_word = Counter(b)
            for k, v in letter_in_word.items():
                letter_count = max(letter_count[k], v)
        res = []
        for a in A:
            letter_in_word = Counter(a)
            for k, v in letter_count.items():
                if letter_in_word.get(k, 0) < v:
                    break
            else:
                 res.append(a)
        return res
            
