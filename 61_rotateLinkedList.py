class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0 or head.next is None:
            return head
        l = 0
        temp = head
        while temp is not None:
            l += 1
            temp = temp.next
        right = head
        left = head
        k = k % l
        if k == 0:
            return head
        pre = right
        l_pre = left
        for _ in range(k):
            right = right.next

        while right is not None:
            l_pre = left
            left = left.next
            pre = right
            right = right.next

        pre.next = head
        head = left
        l_pre.next = None

        return head

a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
a = s.rotateRight(a, 1)
while a:
    print(a.val)
    a = a.next