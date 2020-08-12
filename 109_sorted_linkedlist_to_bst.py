# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def helper(self, root, cur):
        if not cur:
            return None
        new_cur = cur
        if root.left:
            new_cur = self.helper(root.left, cur)
        root.val = new_cur.val
        new_cur = new_cur.next
        if not new_cur:
            return None
        if root.right:
            new_cur = self.helper(root.right, new_cur)
        return new_cur

        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if length == 0:
            return None        
        root = TreeNode(0)
        queue = [root, ]
        length -= 1
        while length != 0:
            cur, queue = queue[0], queue[1:]
            cur.left = TreeNode(0)
            queue.append(cur.left)
            length -= 1
            if length == 0:
                break
            cur.right = TreeNode(0)
            queue.append(cur.right)
            length -= 1
            if length == 0:
                break
        self.helper(root, head)
        return root
        
