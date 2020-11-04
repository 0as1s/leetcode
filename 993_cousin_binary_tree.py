# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, d):
        if root.val == self.x:
            self.xd = d
        if root.val == self.y:
            self.yd = d
        if root.left and root.right:
            if (root.left.val, root.right.val) in ((self.x, self.y), (self.y, self.x)):
                self.xd = -1
                self.yd = -1
        if root.left:
            self.helper(root.left, d+1)
        if root.right:
            self.helper(root.right, d+1)            
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.x = x
        self.y = y
        self.xd = -1
        self.yd = -1

        self.helper(root, 0)
        if self.xd == -1 or self.yd == -1:
            return False
        return self.xd == self.yd