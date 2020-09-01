class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        occurance = set()
        distinct = [1, ]
        if len(s) == 1:
            return 0
        if len(s) == 2:
            return 1 if s[0] == s[1] else 0
        occurance.add(s[0])
        for i in range(1, len(s)):
            if s[i] not in occurance:
                distinct.append(distinct[-1] + 1)
                occurance.add(s[i])
            else:
                distinct.append(distinct[-1])
        occurance = set()
        occurance.add(s[-1])
        reverse_distinct = [1, ]
        for i in range(len(s) - 2, -1, -1):
            if s[i] not in occurance:
                reverse_distinct.insert(0, reverse_distinct[0] + 1)
                occurance.add(s[i])
            else:
                reverse_distinct.insert(0, reverse_distinct[0])
        flag = False
        same = 0
        #print(distinct)
        #print(reverse_distinct)
        for i in range(len(distinct)-1):
            x = distinct[i]
            y = reverse_distinct[i+1]
            if x == y:
                flag = True
                same += 1
            if x != y and flag:
                return same
        return same
