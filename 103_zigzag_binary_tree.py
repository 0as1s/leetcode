# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from queue import deque
        q = deque()
        result = []
        reverse = False
        q.append(root)
        q.append(-1)
        temp = []
        while True:
            cur = q.popleft()
            if cur == -1:
                reverse = not reverse
                result.append(temp)
                temp = []
                if not q:
                    return result
                q.append(-1)
            else:
                if reverse:
                    temp.insert(0, cur.val)
                else:
                    temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
