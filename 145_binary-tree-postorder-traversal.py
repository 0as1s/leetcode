# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        if root.left:
            r.extend(self.postorderTraversal(root.left))
        if root.right:
            r.extend(self.postorderTraversal(root.right))
        r.append(root.val)
        return r
        
