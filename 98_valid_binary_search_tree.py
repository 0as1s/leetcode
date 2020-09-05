# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        
        if root.left and root.right:
            b1, l1, l2 = self.helper(root.left)
            b2, r1, r2 = self.helper(root.right)
            if not (b1 and b2):
                return False, 0, 0
            if not (l1 <= l2 < root.val < r1 <= r2):
                return False, 0, 0
            else:
                return True, l1, r2
        
        if root.left and not root.right:
            b1, l1, l2 = self.helper(root.left)
            if not b1:
                return False, 0, 0
            if not (l1 <= l2 < root.val):
                return False, 0, 0
            else:
                return True, l1, root.val
        
        if root.right and not root.left:
            b2, r1, r2 = self.helper(root.right)
            if not b2:
                return False, 0, 0
            if not (root.val < r1 <= r2):
                return False, 0, 0
            else:
                return True, root.val, r2
            
        if not root.right and not root.left:
            return True, root.val, root.val

        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root)[0]
        