from collections import defaultdict
import random

class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)
        self.l = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if not self.d[val]:
            self.l.append(val)
            self.d[val].add(len(self.l)-1)
            return True
        self.l.append(val)
        self.d[val].add(len(self.l)-1)
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.d[val]:
            return False
        index = self.d[val].pop()
        if index != len(self.l)-1:
            self.l[index] = self.l[-1]
            r = self.l[index]
            self.d[r].remove(len(self.l)-1)
            self.d[r].add(index)
            self.l.pop()
        else:
            self.l.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.l)




        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()

a = RandomizedCollection()
a.insert(1)
a.remove(1)
a.insert(1)