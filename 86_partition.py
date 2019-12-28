# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        pre = ListNode(None)
        new_head = pre
        pre.next = head
        cur = head
        last = None
        while cur:
            if not last and cur.val >= x:
                last = pre
            if last and cur.val < x:
                pre.next = cur.next
                cur.next = last.next
                last.next = cur
                last = cur
                cur = pre.next
                continue
            pre = cur
            cur = cur.next
        return new_head.next

head = ListNode(1)
a = ListNode(4)
b = ListNode(3)
c = ListNode(2)
d = ListNode(5)
e = ListNode(2)
head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
new_head = s.partition(head, 3)
while new_head:
    print(new_head.val)
    new_head = new_head.next

