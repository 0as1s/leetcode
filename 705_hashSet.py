from bisect import bisect_left

class MyHashSet:
    def hash(self, n):
        return n % 107

    def __init__(self):
        self.lists = [[] for _ in range(107)]

    def add(self, key: int) -> None:
        l = self.lists[self.hash(key)]
        i = bisect_left(l, key)
        if i != len(l) and l[i] == key:
            return
        else:
            l.insert(i, key)

    def remove(self, key: int) -> None:
        l = self.lists[self.hash(key)]
        i = bisect_left(l, key)
        if i != len(l) and l[i] == key:
            del l[i]

    def contains(self, key: int) -> bool:
        l = self.lists[self.hash(key)]
        i = bisect_left(l, key)
        return i < len(l) and l[i] == key
