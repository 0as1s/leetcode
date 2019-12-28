class Solution(object):

    def __init__(self):
        self.nums = []

    def findTarget(self, root, k):
        s = set()
        self.go_through(root)
        for i in self.nums:
            if i in s:
                return True
            s.add(k - i)
        return False

    def go_through(self, root):
        if root.left:
            self.go_through(root.left)
        self.nums.append(root.val)
        if root.right:
            self.go_through(root.right)
