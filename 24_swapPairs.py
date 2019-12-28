# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        add = ListNode(-1)
        add.next = head
        cur = add
        first = add.next
        second = first.next
        while first and second:
            cur.next = second
            first.next = second.next
            second.next = first
            cur = first
            first = cur.next
            if first:
                second = first.next
            else:
                second = None
        return add.next


s = Solution()
s.swapPairs()
