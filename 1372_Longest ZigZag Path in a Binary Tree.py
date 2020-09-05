# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution(object):
    def helper(self, root, r_c, l_c):
        self.m = max([self.m, r_c+1, l_c+1])
        if root.left:
            self.helper(root.left, l_c+1, 0)
        if root.right:
            self.helper(root.right, 0, r_c+1)

        
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.m = 1
        self.helper(root, 0, 0)
        return self.m - 1
