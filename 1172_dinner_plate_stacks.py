from collections import defaultdict

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stacks = defaultdict(list)
        self.left=0
        self.right=-1


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.left in self.stacks and len(self.stacks[self.left]) == self.capacity:
            self.left += 1
        if self.left > self.right:
            self.right = self.left
        self.stacks[self.left].append(val)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.right == -1:
            return -1
        while self.right not in self.stacks or len(self.stacks[self.right]) == 0:
            self.right -= 1
            if self.right < 0:
                break
        if self.right < self.left:
            self.left = self.right
        if self.right < 0:
            return -1
        return self.stacks[self.right].pop()

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index not in self.stacks or len(self.stacks[index]) == 0:
            return -1
        if index < self.left:
            self.left = index
        return self.stacks[index].pop()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
