 # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur:
            if cur.val!=pre.val:
                pre.next = cur
                pre = cur
            cur = cur.next
            pre.next = None
        return head

head = ListNode(1)
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
head.next = a
a.next = b
b.next = c
c.next = d

s = Solution()
n = s.deleteDuplicates(head)
while n:
    print(n.val)
    n = n.next