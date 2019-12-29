# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recursive(self, root):
        if not root:
            return "()"
        s = str(root.val)
        left = self.recursive(root.left)
        right = self.recursive(root.right)
        sub = left+right
        if sub == "()()":
            return "(" + s + ")"
        if sub.endswith("()"):
            return "(" + s + sub[:-2] + ")"
        return "(" + s + sub + ")"

    def tree2str(self, t: TreeNode) -> str:
        s = self.recursive(t)
        return s[1:-1]
