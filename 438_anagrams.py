class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict, Counter
        res = []
        diff = set()
        p_dic = defaultdict(int)
        p_dic.update(Counter(p))
        s_dic = defaultdict(int)
        s_dic.update(Counter(s[:len(p)]))

        for k in p_dic:
            if p_dic[k] != s_dic[k]:
                diff.add(k)

        for k in s_dic:
            if p_dic[k] != s_dic[k]:
                diff.add(k)

        if not diff:
            res.append(0)

        for i in range(1, len(s) - len(p) + 1):
            left = s[i-1]
            right = s[i+len(p)-1]
            s_dic[left] -= 1
            s_dic[right] += 1
            if s_dic[left] == p_dic[left] and left in diff:
                diff.remove(left)
            else:
                diff.add(left)
            if s_dic[right] == p_dic[right] and right in diff:
                diff.remove(right)
            else:
                diff.add(right)
            if not diff:
                res.append(i)
        return res

s = Solution()
print(s.findAnagrams("abab", "ab"))
