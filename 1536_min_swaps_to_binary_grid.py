class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lines = []
        pos = dict()
        for i, line in enumerate(grid):
            for j in range(len(line)-1, -1, -1):
                if line[j] == 1 or j == 0:
                    k = j
                    if k == len(line) - 1 and k in pos.keys():
                        return -1
                    while k in pos.keys():
                        k += 1
                    if k < len(grid):
                        pos[k] = i
                    lines.append(k)
                    break
        if len(set(list(pos.keys()))) < len(grid) - 1:
            return -1
        res = 0
        #print(pos)
        #print(lines)
        for j in range(len(grid)-1):
            l = pos[j]
            #print(l)
            res += l - j
            lines[j] = lines[l]
            for i in range(j, l):
                pos[lines[i]] += 1
            for i in range(j, l):
                lines[i+1] = lines[l]
        return res

s = Solution()
# print(s.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))
print(s.minSwaps([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]))