# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, left):
        if self.has == True:
            return
        if not root.left and not root.right and left == 0:
            self.has = True
            return
        if root.left:
            self.helper(root.left, left-root.left.val)
        if root.right:
            self.helper(root.right, left-root.right.val)


    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.has = False
        self.helper(root, sum-root.val)
        return self.has