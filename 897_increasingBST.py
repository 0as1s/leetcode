# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tra(self, root):
        if not root:
            return
        if root.left:
            self.tra(root.left)
        if self.pre:
            self.pre.right = root
        self.pre = root
        if root.right:
            self.tra(root.right)
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.pre = None
        self.tra(root)
        r = root
        while True:
            if not r.left:
                break
            r = r.left
        cur = r
        while cur:
            cur.left = None
            cur = cur.right
        return r


node_1 = TreeNode(1)
node_2 = TreeNode(2)
# node_3 = TreeNode(3)
# node_4 = TreeNode(4)
# node_5 = TreeNode(5)
# node_6 = TreeNode(6)
# node_7 = TreeNode(7)
# node_8 = TreeNode(8)
# node_9 = TreeNode(9)


node_1.right = node_2
# node_1.right = node_3
# node_2.left = node_4
# node_2.right = node_5
# node_3.right = node_6
# node_4.left = node_7
# node_6.left = node_8
# node_6.right = node_9


s = Solution()
s.increasingBST(node_1)