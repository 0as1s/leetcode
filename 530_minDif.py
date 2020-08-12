# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.m = float("Inf")
        self.last = -float("Inf")

        def tra(r):
            if not r:
                return
            tra(r.left)
            self.m = min(self.m, r.val-self.last)
            self.last = r.val
            tra(r.right)
        tra(root)
        return int(self.m)
