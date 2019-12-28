class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findTarget(self, root, k):
        return self.f(root, root.left, k) or self.f(root, root.right, k)

    def f(self, root1, root2, k):
        if not root1 or not root2:
            return False
        # print root1.val, root2.val
        if root1 is root2:
            return self.f(root1.left, root2, k) or self.f(root1.right, root2, k)
        s = root1.val + root2.val
        if s == k:
            return True
        if s < k:
            return self.f(root1.right, root2, k) or self.f(root1, root2.right, k)
        else:
            return self.f(root1.left, root2, k) or self.f(root1, root2.left, k)


root = TreeNode(1)
node1 = TreeNode(0)
node2 = TreeNode(4)
node3 = TreeNode(-2)
node4 = TreeNode(3)
# node5 = TreeNode(7)
root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
# node2.right = node5

s = Solution()
print s.findTarget(root, 7)
