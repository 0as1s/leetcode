class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        storage = dict()
        new_head = Node(head.val)
        storage[id(head)] = new_head
        cur = head
        new_cur = new_head
        while cur != None:
            if cur.next is None:
                new_cur.next = None
            elif id(cur.next) not in storage:
                new_node = Node(cur.next.val)
                storage[id(cur.next)] = new_node
                new_cur.next = new_node
            else:
                new_cur.next = storage[id(cur.next)]
                
            if cur.random is None:
                new_cur.random = None
            elif id(cur.random) not in storage:
                new_node = Node(cur.random.val)
                storage[id(cur.random)] = new_node
                new_cur.random = new_node
            else:
                new_cur.random = storage[id(cur.random)]
            cur = cur.next
            new_cur = new_cur.next
        return new_head
    
