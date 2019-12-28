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
        flag = False
        cur = head.next
        new_head = ListNode(None)
        last = new_head
        while cur:
            if cur.val == pre.val:
                flag = True
            else:
                if not flag:
                    last.next = pre
                    last = pre
                flag = False
            pre.next = None
            pre = cur
            cur = cur.next

        if not flag:
            last.next = pre
        return new_head.next

head = ListNode(3)
a = ListNode(2)
b = ListNode(2)
c = ListNode(2)
d = ListNode(2)
head.next = a
a.next = b
b.next = c
c.next = d

s = Solution()
n = s.deleteDuplicates(head)
while n:
    print(n.val)
    n = n.next