# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        s = [res[0], ]
        for n in res[1:]:
            s.append(s[-1] + n)
        r = set()
        for i in range(len(s)):
            if i in r:
                continue
            for j in range(i, len(s)):
                if j in r:
                    continue
                if s[i] == s[j]:
                    for k in range(i+1, j+1):
                        r.add(k)
        pre = ListNode(0, None)
        init = pre
        cur = head
        count = 0
        while cur:
            temp = cur.next
            if count not in r:
                pre.next = cur
                pre = pre.next
                cur.next = None
            cur = temp
            count += 1
        return init.next
