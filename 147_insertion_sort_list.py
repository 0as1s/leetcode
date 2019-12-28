import time


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        h = ListNode(-1)
        h.next = head
        cur = head
        while(cur and cur.next):
            t = cur.next
            if(t.val > cur.val):
                cur = cur.next
                continue
            pre = h
            while(pre.next and t.val > pre.next.val):
                pre = pre.next
            if pre == cur:
                cur = cur.next
            else:
                cur.next = t.next
                t.next = pre.next
                pre.next = t

        return h.next


pre = ListNode(5000)
head = pre
for i in range(5, -1, -1):
    a = ListNode(i)
    pre.next = a
    pre = pre.next

s = Solution()
a = time.time()
head = s.insertionSortList(head)
b = time.time()
print b-a

while(head):
    print head.val
    head = head.next
