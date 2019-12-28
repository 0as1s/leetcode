from queue import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter(object):
    def __init__(self, root):
        self.root = root
        self.queue = deque()
        self.queue.append(root)
        while self.queue:
            p = self.queue[0]
            if p.left is None:
                break
            elif p.right is None:
                self.queue.append(p.left)
                break
            else:
                self.queue.append(p.left)
                self.queue.append(p.right)
            self.queue.popleft()
    def insert(self, v):
        newNode = TreeNode(v)
        root = self.queue[0]
        if root.left is None:
            root.left = newNode
        else:
            root.right = newNode
            self.queue.popleft()
        self.queue.append(newNode)
        return root.val

    def get_root(self):
        return self.root
