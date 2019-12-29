import queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue.deque()
        self.q2 = queue.deque()
        self.last = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.last is None:
            self.last = x
            return

        self.q1.append(self.last)
        self.last = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.last:
            temp = self.last
            self.last = None
            return temp
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.last:
            return self.last
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.last = self.q1.popleft()
        # self.q2.append(self.last)
        self.q1, self.q2 = self.q2, self.q1
        return self.last

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        print(self.q1, self.q2, self.last)
        if self.q1 or self.q2 or self.last:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
# obj.top()
obj.pop()
obj.top()
print(obj.empty())
obj.pop()
print(obj.empty())