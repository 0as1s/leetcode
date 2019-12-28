# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tra(self, root, L, R):
        if not root:
            return
        if root.left and root.val > L:
            self.tra(root.left, L, R)
        if L <= root.val <= R:
            self.amount += root.val
        if root.right and root.val < R:
            self.tra(root.right, L, R)

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.amount = 0
        self.tra(root, L, R)
        return self.amount
