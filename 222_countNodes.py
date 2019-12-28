from queue import deque

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        q = deque()
        q.append(root)
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return count

