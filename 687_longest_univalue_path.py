# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        left_val, right_val = 0, 0
        m = 1
        s = 1
        if root.left:
            left_val = self.helper(root.left)
            if root.left.val == root.val:
                s += left_val
                m = max(m, left_val+1)
        if root.right:
            right_val = self.helper(root.right)
            if root.right.val == root.val:
                s += right_val
                m = max(m, right_val+1)
        self.m = max(self.m, s)
        return m

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.m = 1
        self.helper(root)
        return self.m-1
        
