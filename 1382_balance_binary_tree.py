# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.nums = []

    def helper(self, root):
        if root.left:
            self.helper(root.left)
        self.nums.append(root.val)
        if root.right:
            self.helper(root.right)
            
    def helper2(self, root, nums):
        if not nums:
            return
        root.val = nums[len(nums) // 2]
        left_nums = nums[0:len(nums) // 2]
        if left_nums:
            new_node = TreeNode()
            root.left = new_node
            self.helper2(root.left, left_nums)
        right_nums = nums[len(nums) // 2 + 1: ]
        if right_nums:
            new_node = TreeNode()
            root.right = new_node
            self.helper2(root.right, right_nums)



    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.helper(root)
        root = TreeNode()
        self.helper2(root, self.nums)
        return root