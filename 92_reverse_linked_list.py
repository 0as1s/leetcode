# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        fake_head = ListNode(-1)
        fake_head.next = head
        left = fake_head
        for _ in range(m-1):
            left = left.next
        begin = left.next
        right = left.next.next
        for _ in range(n-m):
            temp = right.next
            right.next = left.next
            left.next = right
            begin.next = temp
            right = temp
        return fake_head.next


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = None

s = Solution()
head = s.reverseBetween(node_1, 2, 3)
while head:
    print(head.val)
    head = head.next
print(None)