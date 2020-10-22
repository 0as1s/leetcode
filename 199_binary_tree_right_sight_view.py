# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from queue import deque
        q = deque()
        q.append(root)
        q.append(-1)
        pre = None
        r = []
        while q:
            cur = q.popleft()
            if cur == -1:
                if pre == -1:
                    return r
                r.append(pre.val)
                q.append(-1)
            else:
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            pre = cur
