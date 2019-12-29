from typing import List
from queue import deque


class Solution:

    def findCircleNum(self, M: List[List[int]]) -> int:
        s = set(range(len(M)))
        count = 0
        # print(s)
        while s:
            # print(s)
            count += 1
            q = deque()
            q.append(s.pop())
            while q:
                cur = q.popleft()
                for i in range(len(M[cur])):
                    if M[cur][i] == 1and i in s and i != cur:
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