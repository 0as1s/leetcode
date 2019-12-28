class Solution(object):

    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        q = []
        q.append(root)
        s = 0
        while q:
            cur = q[0]
            del(q[0])
            if cur.left:
                if cur.left.left is None and cur.left.right is None:
                    s += cur.left.val
                else:
                    q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return s
