from collections import defaultdict

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if not text:
            return 0
        if len(text) == 1:
            return 1
        count = 1
        squeezed = []
        pre = text[0]
        total = defaultdict(int)
        total[text[0]] += 1

        for i in range(1, len(text)):
            total[text[i]] += 1
            if text[i] != pre:
                squeezed.append((pre, count))
                count = 1
                pre = text[i]
                if i == len(text) - 1:
                    squeezed.append((text[i], 1))
            else:
                count += 1
                if i==len(text) - 1:
                    squeezed.append((pre, count))

        # print(squeezed)
        # print(total)
        m = 0
        for i in range(len(squeezed)):
            if i != 0 and i!=len(squeezed) - 1:
                if squeezed[i-1][0] == squeezed[i+1][0] and squeezed[i][1] == 1:
                    cur = squeezed[i-1][1] + squeezed[i+1][1]
                    if total[squeezed[i-1][0]] > cur:
                        cur += 1
                    m = max(m, cur)
                else:
                    m_self = squeezed[i][1]
                    if total[squeezed[i][0]] > m_self:
                        m_self += 1
                    m = max(m, m_self)

            else:
                m_self = squeezed[i][1]
                if total[squeezed[i][0]] > m_self:
                    m_self += 1
                m = max(m, m_self)
        return m


s = Solution()
print(s.maxRepOpt1("aaabbaaa"))
