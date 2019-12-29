# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        c1 = l1
        c2 = l2
        cur = ListNode("-1")
        head = cur
        while c1 and c2:
            if c1.val < c2.val:
                cur.next = c1
                cur = cur.next
                c1 = c1.next
            else:
                cur.next = c2
                cur = cur.next
                c2 = c2.next

        while c2:
            cur.next = c2
            cur = cur.next
            c2 = c2.next

        while c1:
            cur.next = c1
            cur = cur.next
            c1 = c1.next
        return head.next