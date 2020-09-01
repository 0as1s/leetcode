# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root, res):
    if not root.left and not root.right:
        res.append(root.val)
    if root.left:
        helper(root.left, res)
    if root.right:
        helper(root.right, res)

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        r1 = []
        helper(root1, r1)
        r2 = []
        helper(root2, r2)
        return r1 == r2