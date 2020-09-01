# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from queue import deque
        q = deque()
        s = 0
        q.append((root, False, False))
        while q:
            cur, p, pp = q.popleft()
            if pp:
                s += cur.val
            if cur.left:
                q.append((cur.left, cur.val % 2 == 0, p))
            if cur.right:
                q.append((cur.right, cur.val % 2 == 0, p))
        return s

s = Solution()
s.sumEvenGrandparent()