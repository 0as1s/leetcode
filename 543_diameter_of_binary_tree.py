# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        if not root.left and not root.right:
            return 1
        left, right, cur = 0, 0, 0
        if root.left:
            left = self.helper(root.left) + 1
            cur += (left - 1)
        if root.right:
            right = self.helper(root.right) + 1
            cur += (right - 1)
        self.m = max(self.m, cur)
        return max(left, right)
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.m = 0
        if not root:
            return 0
        self.helper(root)
        return self.m
        
