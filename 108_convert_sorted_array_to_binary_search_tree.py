class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def p(self):
        print self.val
        if self.left:
            self.left.p()
        if self.right:
            self.right.p()


class Solution(object):

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        t = TreeNode(nums[len(nums) / 2])
        t.left = self.sortedArrayToBST(nums[:len(nums) / 2])
        t.right = self.sortedArrayToBST(nums[len(nums) / 2 + 1:])
        return t


a = [1, 2, 3, 4, 5, 6, 7, 8]
s = Solution()
t = s.sortedArrayToBST(a)
t.p()
