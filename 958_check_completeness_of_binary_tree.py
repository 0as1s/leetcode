# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from queue import deque
        if not root:
            return False
        nodes = []
        q = deque()
        q.append(root)
        met_null=False
        add_null=False
        while q:
            cur = q.popleft()
            if met_null and cur != -1:
                return False
            if cur == -1:
                met_null = True
                continue
            if cur.left:
                q.append(cur.left)
            else:
                if not add_null:
                    q.append(-1)
            if cur.right:
                q.append(cur.right)
            else:
                if not add_null:
                    q.append(-1)
        return True
            
