class Solution(object):
    def longestPalindrome(self, s):
        new_s = ["$","#", ]
        for i in s:
            new_s.append(i)
            new_s.append("#")

        mx = 0 # 最右点的右边一个
        id = 0 # 最右mx对应的中心点
        resLen = 0 # 根据p[i]更新全局的最大长度
        resCenter = 0 # 根据p[i]更新全局的中心位置
        p = [0, ] * len(new_s) # 记录在插入了#中的数组中从点i到以i为中心的回文最右侧的长度，这个值减去1就是在没有插入#中的回文串长度
        for i, c in enumerate(new_s):
            if mx > i:
                p[i] = min(p[2 * id - i], mx-i)
            else:
                p[i] = 1
            for j in range(p[i], min(i, len(new_s)-i)):
                if new_s[i+j] != new_s[i-j]:
                    break
                p[i] += 1
            if mx < i + p[i]:
                mx = i + p[i] # p[i]记录的是长度（距离+1），所以mx是回文串最右的右边一个
                id = i
            if resLen < p[i]:
                resLen = p[i]
                resCenter = i
        # print(resLen)
        # print(resCenter)
        # print((resCenter-resLen) // 2, (resCenter-resLen) // 2 + resLen)
        return s[(resCenter-resLen) // 2: (resCenter-resLen) // 2 + resLen - 1]

s = Solution()
print(s.longestPalindrome("cbbd"))