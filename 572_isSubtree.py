# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def test(s_root, t_root):
    if (not s_root and t_root) or (not t_root and s_root):
        return False
    if s_root is None and t_root is None:
        return True
    if s_root.val != t_root.val:
        return False
    return test(s_root.left, t_root.left) and test(s_root.right, t_root.right)


def first_tra(root, t):
    if root is None:
        return False
    if test(root, t):
        return True
    return first_tra(root.left, t) or first_tra(root.right, t)

class Solution(object):

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        return first_tra(s, t)
