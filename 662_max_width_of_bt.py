# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from queue import deque
        q = deque()
        if not root:
            return 0
        q.append(root)
        q.append(-1)
        m = 1
        flag = False
        left = float("Inf")
        right = 0
        count = 0
        buffer = 0
        while q:
            cur = q.popleft()
            if cur == -1:
                m = max(m, right - left + 1)
                if not flag or not q:
                    return m
                q.append(-1)
                flag = False
                left = float("Inf")
                right = 0
                count = 0
                buffer = 0
            else:
                if type(cur) != int:
                    left = min(left, count)
                    right = max(right, count)
                    count += 1
                    if cur.left:
                        q.append(buffer)
                        q.append(cur.left)
                        buffer = 0
                        flag = True
                    else:
                        buffer += 1
                    if cur.right:
                        q.append(buffer)
                        q.append(cur.right)
                        buffer = 0
                        flag = True
                    else:
                        buffer += 1
                else:
                    buffer += 2*cur
                    count += cur
