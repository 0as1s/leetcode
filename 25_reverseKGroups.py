# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head, last):
    # print("enter")
    new_head = ListNode(-1)
    new_last = None
    while True:
        newNode = ListNode(head.val)
        if not new_last:
            new_last = newNode
        newNode.next = new_head.next
        new_head.next = newNode
        # print(last.val)
        if not head or (last and head == last):
            break
        temp = head.next
        head = temp
    return new_head.next, new_last

class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or not head.next:
            return head

        new_head = ListNode(-1)
        new_head.next = head
        cur = new_head
        last = new_head
        while True:
            for i in range(k):
                last = last.next
                if not last:
                    return new_head.next

            cur.next, new_last = reverse(cur.next, last)
            new_last.next = last.next
            cur = new_last
            last = new_last


s = Solution()
node1 = ListNode(1)
node2 = ListNode(7)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(7)
node6 = ListNode(0)
node7 = ListNode(1)
node8 = ListNode(0)
node9 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9



start = s.reverseKGroup(node1, 4)
while start:
    print(start.val)
    start = start.next
