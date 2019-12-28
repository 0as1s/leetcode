# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        if not root:
            return []

        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        pre = []
        self.build_arr(root, pre, 0, result, sum)
        return result

    def build_arr(self, node, pre, total, result, target):
        total = total + node.val
        if node.left or node.right:
            pre.append(node.val)
            if node.left:
                self.build_arr(node.left, pre, total, result, target)
            if node.right:
                self.build_arr(node.right, pre, total, result, target)
            pre.pop()
            return
        elif total == target:
            pre.append(node.val)
            result.append(list(pre))
            pre.pop()


node_5 = TreeNode(5)
node_4 = TreeNode(4)
node_8 = TreeNode(8)
node_11 = TreeNode(11)
node_13 = TreeNode(13)
node_4_2 = TreeNode(4)
node_7 = TreeNode(7)
node_2 = TreeNode(2)
node_5_2 = TreeNode(5)
node_1 = TreeNode(1)


node_11.left = node_7
node_11.right = node_2

node_4_2.left = node_5_2
node_4_2.right = node_1

node_4.left = node_11

node_8.left = node_13
node_8.right = node_4_2

node_5.left = node_4
node_5.right = node_8

node__2 = TreeNode(-2)
node__3 = TreeNode(-3)

node__2.right = node__3

s = Solution()
print s.pathSum(node_5, 22)
print s.pathSum(node__2, -5)
