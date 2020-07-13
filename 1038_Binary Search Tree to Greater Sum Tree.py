# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0
        
    def bstToGstGlobal(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.right:
            self.bstToGst(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.bstToGst(root.left)
        return root
    
    def helper(self, root, val=0, from_right_parent=False):
        sum = 0
        if root.right:
            sum += self.helper(root.right, val)
        sum += root.val
        root.val = sum
        root.val += val
        if root.left:
            sum += self.helper(root.left, val=root.val)
        return sum
            
        
    def bstToGst(self, root):
        if not root:
            return None
        self.helper(root)
        return root
