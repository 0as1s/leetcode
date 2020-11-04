# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        i = 1
        cur = head
        pre = None
        last_even, last_odd=None, None
        while cur.next != None:
            pre = cur
            cur = cur.next
            i += 1
        if i == 1 or i == 2:
            return head
        if i % 2 == 1:
            last_even=None
            last_odd=cur
        else:
            last_even=cur
            last_odd=pre
        last_odd_bak = last_odd
        fake_head=ListNode(0,next=head)
        cur, next = head, head.next
        while True:
            if not cur or not next or cur == last_odd_bak:
                break
            n_cur = next.next
            n_next = n_cur.next if n_cur else None
            cur.next = n_cur
            last_odd.next = next
            last_odd = last_odd.next
            cur, next = n_cur, n_next
        last_odd.next = last_even
        return fake_head.next
            
