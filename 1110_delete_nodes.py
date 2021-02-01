# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque
class Solution(object):
    def go_through(self, root, to_delete):
        if not root:
            return
        if root.left:
            if root.left.val in to_delete:
                self.queue.append(root.left.left)
                self.queue.append(root.left.right)
                root.left = None
            else:
                self.go_through(root.left, to_delete)
        if root.right:
            if root.right.val in to_delete:
                self.queue.append(root.right.left)
                self.queue.append(root.right.right)
                root.right = None
            else:
                self.go_through(root.right, to_delete)
        #self.result.append(root)

    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete = set(to_delete)
        self.queue = deque()
        self.queue.append(root)
        self.result = []
        while self.queue:
            cur = self.queue.popleft()
            if not cur:
                continue
            self.go_through(cur, to_delete)
            self.result.append(cur)
        to_return = []
        while True:
            flag = False
            new_result = []
            for t in self.result:
                if t.val not in to_delete:
                    to_return.append(t)
                else:
                    if t.left:
                        new_result.append(t.left)
                    if t.right:
                        new_result.append(t.right)
                    flag = True

            self.result = new_result
            if not flag:
                break
        return to_return
