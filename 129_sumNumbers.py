# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tra(self, root, current):
        current = current + root.val
        if root.left:
            self.tra(root.left, current * 10)
        if root.right:
            self.tra(root.right, current * 10)
        if not root.left and not root.right:
            self.total += current

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.total = 0
        self.tra(root, 0)
        return self.total


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_4.right = node_5

s = Solution()
print(s.sumNumbers(node_1))
