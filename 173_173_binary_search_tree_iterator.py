# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):

    def __init__(self, root):
        self.nums = []
        if root:
            self.go_through(root)
        self.i = 0
        self.l = len(self.nums)

    def go_through(self, root):
        if root.left:
            self.go_through(root.left)
        self.nums.append(root.val)
        if root.right:
            self.go_through(root.right)

    def hasNext(self):
        if self.i < self.l:
            return True
        return False

    def next(self):
        t = self.nums[self.i]
        self.i += 1
        return t


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
