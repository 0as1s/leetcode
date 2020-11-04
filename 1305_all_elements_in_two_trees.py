# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):            
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        r = []
        stack1 = []
        stack2 = []
        while True:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            if stack1 and stack2:
                if stack1[-1].val <= stack2[-1].val:
                    root1 = stack1.pop()
                    r.append(root1.val)
                    root1 = root1.right
                else:
                    root2 = stack2.pop()
                    r.append(root2.val)
                    root2 = root2.right
            elif stack1:
                root1 = stack1.pop()
                r.append(root1.val)
                root1 = root1.right
            elif stack2:
                root2 = stack2.pop()
                r.append(root2.val)
                root2 = root2.right
            else:
                return r
