# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.stack = []
    def helper(self, root, depth):
        
        if not root.left and not root.right:
            if not self.stack:
                self.stack = [(root, depth), ]
            elif depth > self.stack[0][1]:
                self.stack = [(root, depth), ]
            elif depth == self.stack[0][1]:
                self.stack.append((root, depth))
            else:
                return
        if root.left:
            self.helper(root.left, depth+1)
        if root.right:
            self.helper(root.right, depth+1)
        print(self.stack)
        if (root.left and root.right) and (root.left in self.stack and root.right in self.stack):
            print(self.stack)
            self.stack.append((root, depth))
        
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.helper(root, 0)
        print(self.stack)
        return self.stack[-1][0]