class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root: TreeNode):
        self.cur = root
        self.stack = []
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        temp = self.stack.pop()
        right = temp.right
        while right:
            self.stack.append(right)
            right = right.left
        return temp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.stack else False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()