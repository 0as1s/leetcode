"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [root,]
        r = []
        while stack:
            cur = stack.pop()
            if isinstance(cur, list):
                if len(cur) > 2:
                    stack.append(cur[1:])
                    stack.append(cur[0])
                else:
                    stack.append(cur[1])
                    stack.append(cur[0])
            else:
                if cur.children:
                    if len(cur.children) > 1:
                        if len(cur.children[1:]) == 1:
                            stack.append(cur.children[1])
                        else:
                            stack.append(cur.children[1:])
                    stack.append(cur.children[0])
                r.append(cur.val)
        return r
