# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import tree


class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root


root = tree.list_to_tree([4,2,7,1,3,6,9])
s = Solution()
s.invertTree(root)
print tree.tree_to_list(root)
