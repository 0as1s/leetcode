import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        ListNode.__lt__ = lambda x1, x2: x1.val <= x2.val
        ListNode.__gt__ = lambda x1, x2: x1.val > x2.val

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not any(lists):
            return None
        if not lists:
            return None
        queue = []
        cur = ListNode(-1)
        start = cur
        for l in lists:
            if l:
                heapq.heappush(queue, (l.val, l))
        while queue:
            _, l = heapq.heappop(queue)
            cur.next = l
            cur = cur.next
            if cur.next:
                heapq.heappush(queue, (cur.next.val, cur.next))
        return start.next

s = Solution()
# print(s.mergeKLists([None,]))

s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n1.next = n2
n2.next = n3

n4 = ListNode(1)
n5 = ListNode(1)
n6 = ListNode(2)
n4.next = n5
n5.next = n6

start = s.mergeKLists([n1, n4])
while start:
    print(start.val)
    start = start.next
