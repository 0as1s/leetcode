from collections import defaultdict, Counter

class Solution(object):
    def check(self, d1, d2):
        for k in d1:
            if k not in d2 or d2[k] < d1[k]:
                return False
        return True

    def minWindow(self, s, t):
        indexes = []
        ll = []
        if not s or not t:
            return ""
        for i,c in enumerate(s):
            if c in t:
                indexes.append((c, i))
                ll.append(c)

        counter = Counter(ll)
        counter_2 = Counter(t)
        print(counter)
        print(counter_2)
        if not self.check(counter_2, counter):
            return ""

        counter_3 = defaultdict(int)
        start, end, m = -1, -1, float("inf")
        l, r  = 0, 0
        while True:
            counter_3[indexes[r][0]] += 1
            if self.check(counter_2, counter_3):
                s_, e = indexes[l][-1], indexes[r][-1]
                if e - s_ < m:
                    start, end = s_, e
                    m = e - s_
                while True:
                    if counter_3[indexes[l][0]] > counter_2[indexes[l][0]]:
                        print("check")
                        counter_3[indexes[l][0]] -= 1
                        l += 1
                        s_, e = indexes[l][-1], indexes[r][-1]
                        if e - s_ < m:
                            start, end = s_, e
                            m = e - s_
                    else:
                        break
            r += 1
            if r == len(indexes):
                break

        if m == float("Inf"):
            print("")
            return ""
        print(s[start: end+1])
        return s[start: end+1]

s = Solution()
print(s.minWindow(s = "a", t = "a"))
# s.minWindow(s = "ADOBECODEBANC", t = "ABC")