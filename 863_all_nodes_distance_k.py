# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def find(self, root, target):
        print(root.val, target)
        if root.val == target:
            dis = 0
        else:
            dis = -1
            if root.left:
                dis = max(self.find(root.left, target), dis)
            if root.right:
                dis = max(self.find(root.right, target), dis)
        print(dis)
        if dis != -1:
            self.dis[root.val] = dis
            return dis + 1
        return -1

        
    def helper(self, root, dis, k):
        if root.val in self.dis:
            dis = self.dis[root.val]
        if dis == k:
            self.r.append(root.val)
        if root.left:
            self.helper(root.left, dis+1, k)
        if root.right:
            self.helper(root.right, dis+1, k)

            
        
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.r = []
        self.dis = {}
        self.find(root, target.val)
        print(self.dis)
        self.helper(root, self.dis[root.val], K)
        return self.r