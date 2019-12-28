# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            first = l1
            l1 = l1.next
        else:
            first = l2
            l2 = l2.next

        i = first
        while(True):
            if l1 is None:
                i.next = l2
                return first

            if l2 is None:
                i.next = l1
                return first

            if l1.val <= l2.val:
                i.next = l1
                i = i.next
                l1 = l1.next
            elif l2.val < l1.val:
                i.next = l2
                i = i.next
                l2 = l2.next
