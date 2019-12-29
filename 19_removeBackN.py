# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        last_one = head
        for i in range(n):
            last_one = last_one.next
        if last_one is None:
            head = head.next
            return head
        while last_one.next is not None:
            last_one = last_one.next
            cur = cur.next
        cur.next = cur.next.next
        return head
