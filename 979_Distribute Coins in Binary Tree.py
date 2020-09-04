# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        r = 0
        if root.left:
            r += self.helper(root.left)
        if root.right:
            r += self.helper(root.right)
        r += root.val
        self.r += abs((r - 1))
        return r - 1

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.r = 0
        self.helper(root)
        return self.r