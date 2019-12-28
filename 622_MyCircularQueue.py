class MyCircularQueue(object):
    def __init__(self, k):
        self.queue = [0, ] * k
        self.head = 0
        self.rear = 0
        self.k = k
        self.full = False
        self.empty = True

    def enQueue(self, value):
        if self.full: return False
        self.empty = False
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        if self.rear == self.head:
            self.full = True
        return True

    def deQueue(self):
        if self.empty: return False
        self.head = (self.head + 1) % self.k
        self.full = False
        if self.head == self.rear:
            self.empty = True
        return True

    def Front(self):
        if self.isEmpty(): return -1
        return self.queue[(self.head + 1) % self.k]

    def Rear(self):
        if self.isEmpty(): return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.empty

    def isFull(self):
        return self.full


m = MyCircularQueue(3)
m.enQueue(2)
print(m.deQueue())
print(m.deQueue())
print(m.Rear())
print(m.Front())
