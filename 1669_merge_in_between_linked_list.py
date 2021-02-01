# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        r = ListNode()
        r.next = list1.next
        cur = r
        for i in range(a):
            cur = cur.next
        temp = cur.next
        cur.next = list2.next
        while cur.next:
            cur = cur.next
        for _ in range(b-a):
            temp = temp.next
        cur.next = temp.next
        return r
        
