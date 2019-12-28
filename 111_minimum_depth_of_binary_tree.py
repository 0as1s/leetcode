# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def minDepth(self, root):
        if not root:
            return 0
        import Queue
        q = Queue.Queue()
        q.put((root, 1))
        while q.not_empty:
            cur, depth = q.get()
            if cur.left is None and cur.right is None:
                return depth
            if cur.left:
                q.put((cur.left, depth + 1))
            if cur.right:
                q.put((cur.right, depth + 1))
