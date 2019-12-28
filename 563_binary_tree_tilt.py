# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.t = 0

    def findTilt(self, root):
        if not root:
            return 0
        self.t += abs(self.recursive(root.left) - self.recursive(root.right))
        self.findTilt(root.left)
        self.findTilt(root.right)
        return self.t

    def recursive(self, root):
        if not root:
            return 0
        s = root.val
        if root.left:
            s += self.recursive(root.left)
        if root.right:
            s += self.recursive(root.right)
        return s


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)

node_2.left = node_4
node_1.left = node_2
node_1.right = node_3


s = Solution()
print s.findTilt(node_1)
