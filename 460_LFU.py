class Node(object):
    def __init__(self, key):
        self.next = None
        self.pre = None
        self.key = key

class Block(object):
    def __init__(self, freq):
        self.next = None
        self.pre = None
        self.head = Node(-1)
        self.last = Node(-1)
        self.last.pre = self.head
        self.head.next = self.last
        self.freq = freq

    def insert(self, node):
        self.last.pre.next = node
        node.pre = self.last.pre

        node.next = self.last
        self.last.pre = node

    def transfer(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        if self.next is None or self.next.freq != self.freq+1:
            b = Block(self.freq+1)

            b.next = self.next
            self.next.pre = b

            self.next = b
            self.next.pre = self
        self.next.insert(node)
        if self.head.next == self.last:
            self.pre.next = self.next
            self.next.pre = self.pre
        return self.next

    def remove_top(self):
        node = self.head.next
        key = node.key
        node.pre.next = node.next
        node.next.pre = node.pre
        # self.head.next = self.head.next.next
        if self.head.next == self.last:
            self.pre.next = self.next
            self.next.pre = self.pre
        return key

    def move_to_last(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        self.last.pre.next = node
        node.pre = self.last.pre

        self.last.pre = node
        node.next = self.last

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        self.head = Block(-1)
        self.last = Block(-1)
        self.head.next = self.last
        self.last.pre = self.head

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key in self.d:
            b, n, v = self.d[key]
            new_b = b.transfer(n)
            self.d[key] = (new_b, n, v)
            return v
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # if key in self.d:
        #     b, n, v = self.d[key]
        #     self.d[key] = (b, n, value)
        #     return
        if self.capacity == len(self.d) and key not in self.d:
            k = self.head.next.remove_top()
            del(self.d[k])
        elif key in self.d:
            b, n, v = self.d[key]
            # b.move_to_last(n)
            self.d[key] =(b, n, value)
            self.get(key)
            # print("moved")
            return
        b = self.head.next
        if not b or b.freq != 1:
            b = Block(1)
            b.next = self.head.next
            self.head.next.pre = b

            b.pre = self.head
            self.head.next = b
        n = Node(key)
        b.insert(n)
        self.d[key] = (b, n, value)
