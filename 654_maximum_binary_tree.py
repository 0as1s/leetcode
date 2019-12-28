# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        m = 0
        index = 0
        for i, d in enumerate(nums):
            if d > m:
                index = i
                m = d
        cur = TreeNode(m)
        cur.left = self.constructMaximumBinaryTree(nums[:index])
        cur.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return cur
