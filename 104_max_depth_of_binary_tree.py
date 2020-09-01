# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxDepth(self, root):
        if not root:
            return 0
        q = list()
        q.append((root, 1))
        m = 0
        while q:
            cur, depth = q[0]
            if cur.left is None and cur.right is None:
                if depth > m:
                    m = depth
            if cur.left:
                q.append((cur.left, depth + 1))
            if cur.right:
                q.append((cur.right, depth + 1))
            del q[0]
        return m
