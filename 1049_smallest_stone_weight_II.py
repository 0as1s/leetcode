class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        store = [[0] * len(stones) for _ in stones]
        for i in range(len(stones)):
            store[i][i] = [stones[i]]
        for i in range(len(stones) - 1):
            store[i][i+1] = [abs(stones[i] - stones[i+1])]
        for step in range(2, len(stones)):
            for i in range(0, len(stones) - step):
                res = set()
                flag = False
                for j in range(i, i+step):
                    if flag:
                        break
                    l1 = store[i][j]
                    l2 = store[j+1][i+step]
                    max_delta = max(max(l1) - min(l2), max(l2)-min(l1))
                    flag2 = False
                    for ll1 in l1:
                        for ll2 in l2:
                            res.add(abs(ll1-ll2))
                            if len(res) == max_delta:
                                flag2 = True
                                if len(res) == 100:
                                    flag = True
                                break
                        if flag2:
                            break
                        
                store[i][i+step] = list(res)
        return min(store[0][-1])

s = Solution()
#print(s.lastStoneWeightII([2,7,4,1,8,1]))
store = [0] * 30
from random import randint
for i in range(30):
    store[i] = randint(0, 100)
print(store)
print(s.lastStoneWeightII(store))

        