# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def tra(self, root):
        # print(root.val)
        temp = root.right
        if self.pre:
            self.pre.right = root
        self.pre = root
        if root.left:
            # print("22222222222222")
            # print(root.val)
            # print(root.left.val)
            # print(self.pre.val)
            # print("22222222222222")
            self.tra(root.left)
        if temp:
            # print("111111111111")
            # print(root.val)
            # print(root.right.val)
            # print(self.pre.val)
            # print("111111111111")
            self.tra(temp)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.pre = None
        self.tra(root)

        while root:
            root.left = None
            root = root.right


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a_1 = TreeNode(1)
b_2 = TreeNode(2)
c_5 = TreeNode(5)
d_3 = TreeNode(3)
e_4 = TreeNode(4)
f_6 = TreeNode(6)

a_1.left = b_2
a_1.right = c_5
b_2.left = d_3
b_2.right = e_4
c_5.right = f_6


s = Solution()
s.flatten(a_1)