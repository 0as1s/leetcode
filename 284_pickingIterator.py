# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.pick = False
        self.top = None

    def peek(self):
        if self.pick:
            return self.top
        self.top = self.iterator.next()
        self.pick = True
        return self.top

    def next(self):
        if self.pick:
            self.pick = False
            return self.top
        return self.iterator.next()

    def hasNext(self):
        return self.pick or self.iterator.hasNext()
