class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        group_by_length = defaultdict(list)
        for w in words:
            group_by_length[len(w)].append(w)
        keys = sorted(list(group_by_length.keys()))
        transfer_map = defaultdict(dict)

        for k in keys:
            source = group_by_length[k]
            target = group_by_length[k+1]
            for s in source:
                for t in target:
                    for i in range(len(t)):
                        if t[0:i] + t[i+1:] == s:
                            transfer_map[k+1][t] = s
                            break
        lengths = defaultdict(int)
        for w in group_by_length[keys[0]]:
            lengths[w] = 1
        for k in keys[1:]:
            words = group_by_length[k]
            for w in words:
                if w not in transfer_map[k]:
                    lengths[w] = 1
                    continue
                lengths[w] = lengths[transfer_map[k][w]] + 1
        return max(lengths.values())

s = Solution()
print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))