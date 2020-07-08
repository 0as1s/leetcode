# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        stack = []
        cur = head
        n = 0
        while cur:
            stack.append(cur)
            cur = cur.next
            n += 1
        cur = head
        while len(stack) > (n+1)//2:
            last = stack.pop()
            last.next = cur.next
            cur.next = last
            cur = last.next
        cur.next = None
