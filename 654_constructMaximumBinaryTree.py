# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def node(self, l):
        if len(l) == 1:
            return TreeNode(l[0])
        m = l[0]
        m_i = 0
        for i, v in enumerate(l):
            if v > m:
                m_i = i
                m = v
        root = TreeNode(m)
        if m_i != 0:
            root.left = self.node(list(l[:m_i]))
        if m_i < len(l) - 1:
            root.right = self.node(list(l[m_i+1:]))
        return root

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.node(nums)
        return root

s = Solution()
s.constructMaximumBinaryTree([3,2,1,6,0,5])
