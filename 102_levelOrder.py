from queue import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        q.append(-1)
        r = []
        while q:
            t = q.popleft()
            if t == -1:
                result.append(r)
                r = []
                if not q:
                    break
                q.append(-1)
            else:
                r.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        return result


