# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = 0
        from queue import deque
        q = deque()
        q.append(root)
        q.append(-1)
        while q:
            cur = q.popleft()
            if cur == -1:
                if not q:
                    return s
                s = 0
                q.append(-1)
            else:
                s += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)