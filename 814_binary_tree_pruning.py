# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        n = root.val
        if root.left:
            l = self.helper(root.left)
            if l == 0:
                root.left = None
            n += l
        if root.right:
            r = self.helper(root.right)
            if r == 0:
                root.right = None
            n += r
        return n
        
        
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        n = self.helper(root)
        if n == 0:
            return None
        return root
        