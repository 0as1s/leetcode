# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.target = None
    def helper(self, root, p, q):
        if self.target:
            return (False, False)
        self_r = (root.val == p.val, root.val == q.val)
        left_r = self.helper(root.left, p, q)
        right_r = self.helper(root.right, p, q)
        result = (self_r[0] or left_r[0] or right_r[0], self_r[1] or left_r[1] or right_r[1])
        if self.target:
            return (True, True)
        if result[0] and result[1]:
            self.target = root
            return (True, True)
        return result

        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, p, q)
        return self.target
