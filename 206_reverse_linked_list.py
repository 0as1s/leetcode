# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        new_head = None
        while head:
            n = ListNode(head.val)
            n.next = new_head
            new_head = n
            head = head.next
        return new_head