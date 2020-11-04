# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, cur):
        cur.append(str(root.val))
        if root.left:
            self.helper(root.left, cur)
            cur.pop()
        if root.right:
            self.helper(root.right, cur)
            cur.pop()
        if not root.left and not root.right:
            self.r.append("->".join(cur))
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.r = []
        self.helper(root, [])
        return self.r
        