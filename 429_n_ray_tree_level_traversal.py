"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        from queue import deque
        q = deque()
        q.append(root)
        q.append(-1)
        res = []
        temp = []
        while True:
            cur = q.popleft()
            if cur == -1:
                if not q:
                    res.append(temp)
                    break
                q.append(-1)
                #print(temp)
                res.append(temp)
                temp = []
            else:
                # print(cur.val)
                temp.append(cur.val)
                for c in cur.children:
                    q.append(c)
        
        return res
