from typing import List
from queue import deque
from collections import defaultdict


class Solution:

    def findCircleNum(self, M: List[List[int]]) -> int:
        s = set(range(len(M)))
        count = 0
        # print(s)
        friends = defaultdict(list)
        for i in range(len(M)):
            for j in range(len(M)):
                if j != i and M[i][j] == 1:
                    friends[i].append(j)
        while s:
            # print(s)
            count += 1
            q = deque()
            q.append(s.pop())
            while q:
                cur = q.popleft()
                for i in friends[cur]:
                    if i in s:
                        q.append(i)
                        s.remove(i)
                # print(s)
        return count


M = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]
M = [[1,1,0],[1,1,0],[0,0,1]]
s = Solution()
print(s.findCircleNum(M))