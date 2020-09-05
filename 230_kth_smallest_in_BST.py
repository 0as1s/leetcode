# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import *

class Solution(object):
    def helper(self, root, k, heap):
        if -root.val > heap[0]:
            if len(heap) == k:
                heappushpop(heap, -root.val)
            else:
                heappush(heap, -root.val)
        if root.left:
            self.helper(root.left, k, heap)
        if root.right:
            self.helper(root.right, k, heap)


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        r = []
        self.helper(root, k, r)
        return heappop(r)
