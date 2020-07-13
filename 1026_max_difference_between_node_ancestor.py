# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def top_down(self, root, max_, min_):
        root.max_from_top = max(max_, root.val)
        root.min_from_top = min(min_, root.val)
        if root.left:
            self.top_down(root.left, root.max_from_top, root.min_from_top)
        if root.right:
            self.top_down(root.right, root.max_from_top, root.min_from_top)

    def buttom_up(self, root):
        min_, max_ = root.val, root.val
        if root.left:
            min_1, max_1 = self.buttom_up(root.left)
            min_ = min(min_1, min_)
            max_ = max(max_1, max_)
            
        if root.right:
            min_1, max_1 = self.buttom_up(root.right)
            min_ = min(min_1, min_)
            max_ = max(max_1, max_)

        root.max_from_buttom = max_
        root.min_from_buttom = min_

        return root.min_from_buttom, root.max_from_buttom

    def helper(self, root):
        max_diff = max(abs(root.max_from_buttom - root.min_from_top), abs(root.min_from_buttom - root.max_from_top))
        if root.left:
            max_diff = max(max_diff, self.helper(root.left))
        if root.right:
            max_diff = max(max_diff, self.helper(root.right))
        return max_diff


    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.top_down(root, -float("Inf"), float("Inf"))
        self.buttom_up(root)
        return self.helper(root)
