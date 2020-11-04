# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def helper(self, l1, l2):
        if l1.next != None:
            c = self.helper(l1.next, l2.next)
            n_r = (l1.val + l2.val + c) % 10
            n_c = (l1.val + l2.val + c) // 10
            n = ListNode(n_r, self.r)
            self.r = n
            return n_c
        else:
            n_r = (l1.val + l2.val) % 10
            n_c = (l1.val + l2.val) // 10
            n = ListNode(n_r, self.r)
            self.r = n
            return n_c


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1, ll2 = 0, 0
        l1_head = l1
        l2_head = l2
        while(l1_head):
            ll1 += 1
            l1_head = l1_head.next
        while(l2_head):
            ll2 += 1
            l2_head = l2_head.next

        if ll1 < ll2:
            ll1, ll2 = ll2, ll1
            l1, l2 = l2, l1
            
        for i in range(ll1-ll2):
            n = ListNode(0, l2)
            l2 = n
        self.r = None

        c = self.helper(l1, l2)
        if c != 0:
            n_r = ListNode(1, self.r)
            self.r = n_r
        
        return self.r
